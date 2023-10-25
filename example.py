def calc_dry_gas_constant():
    m_n2 = 28.0134
    m_o2 = 31.9988
    m_ar = 39.948
    m_co2 = 44.0095

    n_n2 = 0.78084
    n_o2 = 0.20946
    n_ar = 0.00934
    n_co2 = 0.000314

    m_avg = (m_n2 * n_n2) + (m_o2 * n_o2) + (m_ar * n_ar) + (m_co2 * n_co2)

    print(m_avg)

    R = 8.31446261815324
    R_dry = R / (m_avg/1000)
    return R_dry

if __name__ == '__main__':
    print(calc_dry_gas_constant())