// ILI9341 SPI Display Test
// Simple hardware validation for Radxa Zero 3W or Raspberry Pi
// Draws solid colors (red/green/blue/white/black) to verify SPI + GPIO

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/spi/spidev.h>
#include <sys/ioctl.h>
#include <string.h>
#include <gpiod.h>

#define SPI_DEVICE      "/dev/spidev0.0"
#define SPI_SPEED       32000000   // 32MHz for ILI9341
#define DC_PIN          25         // Example GPIO for D/C
#define RST_PIN         24         // Example GPIO for RESET
#define CHIPNAME        "gpiochip0"

static int spi_fd;
static struct gpiod_chip *chip;
static struct gpiod_line *dc_line;
static struct gpiod_line *rst_line;

void gpio_write(struct gpiod_line *line, int value) {
    gpiod_line_set_value(line, value);
}

void spi_write_cmd(uint8_t cmd) {
    gpio_write(dc_line, 0); // Command mode
    write(spi_fd, &cmd, 1);
}

void spi_write_data(uint8_t data) {
    gpio_write(dc_line, 1); // Data mode
    write(spi_fd, &data, 1);
}

void spi_write_data_buf(uint8_t *buf, size_t len) {
    gpio_write(dc_line, 1);
    write(spi_fd, buf, len);
}

void ili9341_reset() {
    gpio_write(rst_line, 0);
    usleep(200000);
    gpio_write(rst_line, 1);
    usleep(200000);
}

void ili9341_init() {
    // Minimal required init
    spi_write_cmd(0x01); // Software Reset
    usleep(500000);

    spi_write_cmd(0x28); // Display OFF
    spi_write_cmd(0x3A); // Pixel Format
    spi_write_data(0x55); // 16-bit color
    spi_write_cmd(0x36); // MADCTL
    spi_write_data(0x48); // Row/col order
    spi_write_cmd(0x29); // Display ON
}

void set_addr_window(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1) {
    spi_write_cmd(0x2A);
    spi_write_data(x0 >> 8);
    spi_write_data(x0 & 0xFF);
    spi_write_data(x1 >> 8);
    spi_write_data(x1 & 0xFF);

    spi_write_cmd(0x2B);
    spi_write_data(y0 >> 8);
    spi_write_data(y0 & 0xFF);
    spi_write_data(y1 >> 8);
    spi_write_data(y1 & 0xFF);

    spi_write_cmd(0x2C);
}

void fill_screen(uint16_t color) {
    uint16_t width = 240;
    uint16_t height = 320;

    set_addr_window(0, 0, width - 1, height - 1);

    uint8_t buffer[240 * 2];
    for (int i = 0; i < sizeof(buffer) / 2; i++) {
        buffer[2*i]   = color >> 8;
        buffer[2*i+1] = color & 0xFF;
    }

    for (int y = 0; y < height; y++) {
        spi_write_data_buf(buffer, sizeof(buffer));
    }
}

int main() {
    // ---- SPI ----
    spi_fd = open(SPI_DEVICE, O_RDWR);
    if (spi_fd < 0) {
        perror("SPI open failed");
        return 1;
    }

    uint32_t mode = SPI_MODE_0;
    ioctl(spi_fd, SPI_IOC_WR_MODE, &mode);
    ioctl(spi_fd, SPI_IOC_WR_MAX_SPEED_HZ, &SPI_SPEED);

    // ---- GPIO ----
    chip = gpiod_chip_open_by_name(CHIPNAME);
    dc_line = gpiod_chip_get_line(chip, DC_PIN);
    rst_line = gpiod_chip_get_line(chip, RST_PIN);

    gpiod_line_request_output(dc_line, "dc", 0);
    gpiod_line_request_output(rst_line, "rst", 1);

    // ---- Init Sequence ----
    ili9341_reset();
    ili9341_init();

    // ---- Color Test ----
    fill_screen(0xF800); // Red
    sleep(1);
    fill_screen(0x07E0); // Green
    sleep(1);
    fill_screen(0x001F); // Blue
    sleep(1);
    fill_screen(0xFFFF); // White
    sleep(1);
    fill_screen(0x0000); // Black
    sleep(1);

    close(spi_fd);
    gpiod_chip_close(chip);

    return 0;
}
