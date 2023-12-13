from enum import Enum, unique


@unique
class X(str, Enum):
    """
    Column Names as Constants of: data/exoplanet/exoplanet_eu_catalog.csv

    Created with: "https://github.com/eugen-hoppe/pattern/blob/main/v3/csv_const/README.md"
    """

    NAME: str = "name"
    PLANET_STATUS: str = "planet_status"
    MASS: str = "mass"
    MASS_ERROR_MIN: str = "mass_error_min"
    MASS_ERROR_MAX: str = "mass_error_max"
    MASS_SINI: str = "mass_sini"
    MASS_SINI_ERROR_MIN: str = "mass_sini_error_min"
    MASS_SINI_ERROR_MAX: str = "mass_sini_error_max"
    RADIUS: str = "radius"
    RADIUS_ERROR_MIN: str = "radius_error_min"
    RADIUS_ERROR_MAX: str = "radius_error_max"
    ORBITAL_PERIOD: str = "orbital_period"
    ORBITAL_PERIOD_ERROR_MIN: str = "orbital_period_error_min"
    ORBITAL_PERIOD_ERROR_MAX: str = "orbital_period_error_max"
    SEMI_MAJOR_AXIS: str = "semi_major_axis"
    SEMI_MAJOR_AXIS_ERROR_MIN: str = "semi_major_axis_error_min"
    SEMI_MAJOR_AXIS_ERROR_MAX: str = "semi_major_axis_error_max"
    ECCENTRICITY: str = "eccentricity"
    ECCENTRICITY_ERROR_MIN: str = "eccentricity_error_min"
    ECCENTRICITY_ERROR_MAX: str = "eccentricity_error_max"
    INCLINATION: str = "inclination"
    INCLINATION_ERROR_MIN: str = "inclination_error_min"
    INCLINATION_ERROR_MAX: str = "inclination_error_max"
    ANGULAR_DISTANCE: str = "angular_distance"
    DISCOVERED: str = "discovered"
    UPDATED: str = "updated"
    OMEGA: str = "omega"
    OMEGA_ERROR_MIN: str = "omega_error_min"
    OMEGA_ERROR_MAX: str = "omega_error_max"
    TPERI: str = "tperi"
    TPERI_ERROR_MIN: str = "tperi_error_min"
    TPERI_ERROR_MAX: str = "tperi_error_max"
    TCONJ: str = "tconj"
    TCONJ_ERROR_MIN: str = "tconj_error_min"
    TCONJ_ERROR_MAX: str = "tconj_error_max"
    TZERO_TR: str = "tzero_tr"
    TZERO_TR_ERROR_MIN: str = "tzero_tr_error_min"
    TZERO_TR_ERROR_MAX: str = "tzero_tr_error_max"
    TZERO_TR_SEC: str = "tzero_tr_sec"
    TZERO_TR_SEC_ERROR_MIN: str = "tzero_tr_sec_error_min"
    TZERO_TR_SEC_ERROR_MAX: str = "tzero_tr_sec_error_max"
    LAMBDA_ANGLE: str = "lambda_angle"
    LAMBDA_ANGLE_ERROR_MIN: str = "lambda_angle_error_min"
    LAMBDA_ANGLE_ERROR_MAX: str = "lambda_angle_error_max"
    IMPACT_PARAMETER: str = "impact_parameter"
    IMPACT_PARAMETER_ERROR_MIN: str = "impact_parameter_error_min"
    IMPACT_PARAMETER_ERROR_MAX: str = "impact_parameter_error_max"
    TZERO_VR: str = "tzero_vr"
    TZERO_VR_ERROR_MIN: str = "tzero_vr_error_min"
    TZERO_VR_ERROR_MAX: str = "tzero_vr_error_max"
    K: str = "k"
    K_ERROR_MIN: str = "k_error_min"
    K_ERROR_MAX: str = "k_error_max"
    TEMP_CALCULATED: str = "temp_calculated"
    TEMP_CALCULATED_ERROR_MIN: str = "temp_calculated_error_min"
    TEMP_CALCULATED_ERROR_MAX: str = "temp_calculated_error_max"
    TEMP_MEASURED: str = "temp_measured"
    HOT_POINT_LON: str = "hot_point_lon"
    GEOMETRIC_ALBEDO: str = "geometric_albedo"
    GEOMETRIC_ALBEDO_ERROR_MIN: str = "geometric_albedo_error_min"
    GEOMETRIC_ALBEDO_ERROR_MAX: str = "geometric_albedo_error_max"
    LOG_G: str = "log_g"
    PUBLICATION: str = "publication"
    DETECTION_TYPE: str = "detection_type"
    MASS_DETECTION_TYPE: str = "mass_detection_type"
    RADIUS_DETECTION_TYPE: str = "radius_detection_type"
    ALTERNATE_NAMES: str = "alternate_names"
    MOLECULES: str = "molecules"
    STAR_NAME: str = "star_name"
    RA: str = "ra"
    DEC: str = "dec"
    MAG_V: str = "mag_v"
    MAG_I: str = "mag_i"
    MAG_J: str = "mag_j"
    MAG_H: str = "mag_h"
    MAG_K: str = "mag_k"
    STAR_DISTANCE: str = "star_distance"
    STAR_DISTANCE_ERROR_MIN: str = "star_distance_error_min"
    STAR_DISTANCE_ERROR_MAX: str = "star_distance_error_max"
    STAR_METALLICITY: str = "star_metallicity"
    STAR_METALLICITY_ERROR_MIN: str = "star_metallicity_error_min"
    STAR_METALLICITY_ERROR_MAX: str = "star_metallicity_error_max"
    STAR_MASS: str = "star_mass"
    STAR_MASS_ERROR_MIN: str = "star_mass_error_min"
    STAR_MASS_ERROR_MAX: str = "star_mass_error_max"
    STAR_RADIUS: str = "star_radius"
    STAR_RADIUS_ERROR_MIN: str = "star_radius_error_min"
    STAR_RADIUS_ERROR_MAX: str = "star_radius_error_max"
    STAR_SP_TYPE: str = "star_sp_type"
    STAR_AGE: str = "star_age"
    STAR_AGE_ERROR_MIN: str = "star_age_error_min"
    STAR_AGE_ERROR_MAX: str = "star_age_error_max"
    STAR_TEFF: str = "star_teff"
    STAR_TEFF_ERROR_MIN: str = "star_teff_error_min"
    STAR_TEFF_ERROR_MAX: str = "star_teff_error_max"
    STAR_DETECTED_DISC: str = "star_detected_disc"
    STAR_MAGNETIC_FIELD: str = "star_magnetic_field"
    STAR_ALTERNATE_NAMES: str = "star_alternate_names"

    @staticmethod
    def path():
        return "data/exoplanet/exoplanet_eu_catalog.csv"
