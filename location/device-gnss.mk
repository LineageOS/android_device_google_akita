# include common gnss binaries
-include vendor/samsung_slsi/gps/s5300/gnss_release.mk

# include customized gps config files
PRODUCT_COPY_FILES += \
    device/google/akita/location/ca.pem:vendor/etc/gnss/ca.pem

ifneq (,$(filter userdebug eng, $(TARGET_BUILD_VARIANT)))
    PRODUCT_COPY_FILES += \
        device/google/akita/location/gps.cfg:vendor/etc/gnss/gps.cfg
    PRODUCT_VENDOR_PROPERTIES += \
        vendor.gps.aol.enabled=true
else
    PRODUCT_COPY_FILES += \
        device/google/akita/location/gps_user.cfg:vendor/etc/gnss/gps.cfg
endif

# include pixel gnss hal service
-include vendor/google_devices/gs-common/proprietary/gps/pixel_gnss_hal.mk
