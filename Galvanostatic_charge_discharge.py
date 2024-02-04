import pandas as pd


df_gcd = pd.read_csv("teste_GCD.csv")


max_volt_index = df_gcd["Voltage (V)"].idxmax()

initial_voltage = df_gcd["Voltage (V)"][max_volt_index + 2]

final_voltage = df_gcd["Voltage (V)"].iloc[-1]


initial_time = df_gcd.loc[max_volt_index, 'Time (s)']

final_time = df_gcd["Time (s)"].iloc[-1]


discharge_current = (50e-6) #The value of the discharge current needs to be set manually (in Amps)

capacitance = (discharge_current*(final_time - initial_time))/(initial_voltage - final_voltage)

print(f"The device's capacitance is {capacitance}")


