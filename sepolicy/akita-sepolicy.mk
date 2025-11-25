# sepolicy exclusively for akita.
BOARD_SEPOLICY_DIRS += device/google/akita/sepolicy/aam
BOARD_SEPOLICY_DIRS += device/google/akita/sepolicy/vendor
BOARD_SEPOLICY_DIRS += device/google/akita/sepolicy/tracking_denials
BOARD_SEPOLICY_DIRS += device/google/akita/sepolicy/radio

BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/bcmbt/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/gps/pixel/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/gril/common/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/modem/radio_ext/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/touch/gti/ical/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/touch/gti/predump_sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/touch/predump/sepolicy
BOARD_VENDOR_SEPOLICY_DIRS += device/google/gs-common/wireless_charger/sepolicy

BOARD_VENDOR_SEPOLICY_DIRS += hardware/google/pixel-sepolicy/powerstats
BOARD_VENDOR_SEPOLICY_DIRS += hardware/google/pixel-sepolicy/vibrator/common
BOARD_VENDOR_SEPOLICY_DIRS += hardware/google/pixel-sepolicy/vibrator/cs40l26
