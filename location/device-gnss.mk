# include common gnss binaries
-include vendor/samsung_slsi/gps/s5300/gnss_release.mk

DEVICE_PRODUCT_COMPATIBILITY_MATRIX_FILE += \
    device/google/akita/location/device_framework_matrix_product.xml

# include customized gps config files
PRODUCT_COPY_FILES += \
    device/google/akita/location/ca.pem:vendor/etc/gnss/ca.pem

PRODUCT_COPY_FILES += \
    device/google/akita/location/gps_user.cfg:vendor/etc/gnss/gps.cfg

# include pixel gnss hal service
-include vendor/google_devices/gs-common/proprietary/gps/pixel_gnss_hal.mk
