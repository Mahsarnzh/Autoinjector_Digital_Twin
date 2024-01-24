import streamlit as st

class AutoinjectorAlarm:
    def __init__(self, temperature_threshold, exposed_to_heat=False, exposed_to_sunlight=False,
                 shaken=False, cap_removed=False, expired=False):
        self.temperature_threshold = temperature_threshold
        self.exposed_to_heat = exposed_to_heat
        self.exposed_to_sunlight = exposed_to_sunlight
        self.shaken = shaken
        self.cap_removed = cap_removed
        self.expired = expired

    def check_temperature(self, current_temperature):
        if current_temperature > self.temperature_threshold:
            st.warning("Alarm: Temperature exceeds the threshold!")

    def check_exposure_to_heat(self):
        if self.exposed_to_heat:
            st.warning("Alarm: Exposed to heat source!")

    def check_exposure_to_sunlight(self):
        if self.exposed_to_sunlight:
            st.warning("Alarm: Exposed to sunlight!")

    def check_shaking(self):
        if self.shaken:
            st.warning("Alarm: Shaking detected!")

    def check_cap_removal(self):
        if self.cap_removed:
            st.warning("Alarm: Cap has been removed!")

    def check_expiration(self):
        if self.expired:
            st.warning("Alarm: Autoinjector has expired!")

def main():
    st.title("Autoinjector Monitoring App")

    # Receive user input for temperature and checkboxes
    current_temperature = st.slider("Current Temperature", min_value=0, max_value=50, value=25, step=1)
    exposed_to_heat = st.checkbox("Exposed to Heat")
    exposed_to_sunlight = st.checkbox("Exposed to Sunlight")
    shaken = st.checkbox("Shaking Detected")
    cap_removed = st.checkbox("Cap Removed")
    expired = st.checkbox("Autoinjector Expired")

    # Create an instance of AutoinjectorAlarm
    autoinjector_alarm = AutoinjectorAlarm(
        temperature_threshold=30,
        exposed_to_heat=exposed_to_heat,
        exposed_to_sunlight=exposed_to_sunlight,
        shaken=shaken,
        cap_removed=cap_removed,
        expired=expired
    )

    # Display alarm messages
    autoinjector_alarm.check_temperature(current_temperature)
    autoinjector_alarm.check_exposure_to_heat()
    autoinjector_alarm.check_exposure_to_sunlight()
    autoinjector_alarm.check_shaking()
    autoinjector_alarm.check_cap_removal()
    autoinjector_alarm.check_expiration()

if __name__ == "__main__":
    main()
