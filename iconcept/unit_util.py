
class UnitUtil:
    KM_MILE_RATIO = 0.62137
    CM_INCH_RATIO = 0.3937
    KG_POUND_RATIO = 2.20462

    @staticmethod
    def km2mile(km):
        return km * UnitUtil.KM_MILE_RATIO

    @staticmethod
    def mile2km(mile):
        return mile / UnitUtil.KM_MILE_RATIO

    @staticmethod
    def cm2inch(cm):
        return cm * UnitUtil.CM_INCH_RATIO

    @staticmethod
    def inch2cm(inch):
        return inch / UnitUtil.CM_INCH_RATIO

    @staticmethod
    def kg2pound(kg):
        return kg * UnitUtil.KG_POUND_RATIO

    @staticmethod
    def pound2kg(pound):
        return pound / UnitUtil.KG_POUND_RATIO
