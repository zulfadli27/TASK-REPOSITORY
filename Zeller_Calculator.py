 Contoh Program Python: Zeller Calculator
def zeller_congruence(day, month, year):
    # Adjustments for January and February
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

    # Mapping hasil ke nama hari
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

# Input dari pengguna
day = int(input("Masukkan tanggal (1-31): "))
month = int(input("Masukkan bulan (1-12): "))
year = int(input("Masukkan tahun (contoh: 2025): "))

# Hitung hari
day_name = zeller_congruence(day, month, year)
print(f"Hari dalam minggu untuk {day}-{month}-{year} adalah: {day_name}")
