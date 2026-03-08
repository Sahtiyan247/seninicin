# Başlangıçta cevabı yanlış kabul ediyoruz
cevap = ""

# Cevap "dünya kadınlar günü" olmadığı sürece döngü devam eder
while cevap.lower().strip() != "dünya kadınlar günü":
    cevap = input("Bu gün günlerden ne? ")
    
    if cevap.lower().strip() == "dünya kadınlar günü":
        print("Dünyanın en güzel kadınının dünya kadınlar günü kutlu olsunnnnnn")
        break # Doğru bilince döngüden çık
    else:
        print("Yanlışşşşş! Tekrar dene...")
