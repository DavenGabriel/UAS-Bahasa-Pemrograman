def convert(s):
    try:
        x = int(s)
        print("Konversi berhasil! \nx=", x)
    except ValueError:
        print("Konversi gagal!")

convert("12")