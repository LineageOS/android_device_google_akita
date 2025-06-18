DEVICE_PRODUCT_COMPATIBILITY_MATRIX_FILE += \
    device/google/akita/location/device_framework_matrix_product.xml

# include customized gps config files
PRODUCT_COPY_FILES += \
    device/google/akita/location/ca.pem:vendor/etc/gnss/ca.pem

PRODUCT_COPY_FILES += \
    device/google/akita/location/gps_user.cfg:vendor/etc/gnss/gps.cfg
