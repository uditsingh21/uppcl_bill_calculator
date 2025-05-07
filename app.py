import streamlit as st


def calculate_uppcl_bill(units_consumed, load_kw):
    # Unit charges based on slab
    if units_consumed <= 100:
        unit_charge = units_consumed * 4
    elif units_consumed <= 300:
        unit_charge = (100 * 4) + (units_consumed - 100) * 6
    else:
        unit_charge = (100 * 4) + (200 * 6) + (units_consumed - 300) * 8

    # Fixed charge
    fixed_charge = load_kw * 110

    # Electricity duty (~5%)
    electricity_duty = 0.05 * unit_charge

    # Estimated surcharges
    other_surcharges = 75

    # Total
    total = unit_charge + fixed_charge + electricity_duty + other_surcharges

    return unit_charge, fixed_charge, electricity_duty, other_surcharges, total


st.title("💡 UPPCL Bill Estimator")

units = st.number_input("Enter units consumed", min_value=0)
load = st.number_input("Enter load in kW", min_value=1, max_value=10)

if st.button("Calculate"):
    uc, fc, ed, sc, total = calculate_uppcl_bill(units, load)

    st.markdown(f"### 🔍 Bill Breakdown:")
    st.write(f"• Unit Charges: ₹{uc:.2f}")
    st.write(f"• Fixed Charges: ₹{fc:.2f}")
    st.write(f"• Electricity Duty (5%): ₹{ed:.2f}")
    st.write(f"• Other Surcharges: ₹{sc:.2f}")
    st.markdown(f"## 💰 Estimated Total: ₹{total:.2f}")
