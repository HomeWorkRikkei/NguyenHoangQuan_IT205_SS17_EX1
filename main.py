raw_logs = []
processed_logs = []

def add_data():
    global raw_logs
    print("\n--- NẠP DỮ LIỆU LOG ---")
    raw_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
    
    if not raw_input.strip():
        print("Dữ liệu nhập vào trống.")
        return

    special_digi = "!@#$"
    mapping_table = str.maketrans("", "", special_digi)
    cleaned_input = raw_input.translate(mapping_table)
    
    raw_logs = [log.strip() for log in cleaned_input.split(";") if log.strip()]
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

def filter_high_alerts():
    global processed_logs
    print("\n--- L LỌC CẢNH BÁO ---")
    
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    processed_logs = [
        log for log in raw_logs 
        if "error" in log.lower() or "critical" in log.lower()
    ]
    
    if processed_logs:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")
    else:
        print("Không tìm thấy cảnh báo nguy hiểm nào (ERROR/CRITICAL).")

def mask_ip_addresses():
    """Chức năng 3: Mã hóa địa chỉ IP (Masking) và hiển thị báo cáo an toàn"""
    print("\n--- MẠH HÓA IP ---")
    
    if not processed_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    masked_logs = []
    
    for log in processed_logs:
        words = log.split()
        new_words = []
        for word in words:
            clean_word = word.strip(".,;:!")
            if clean_word.count('.') == 3 and all(c.isdigit() for c in clean_word.split('.')):
                ip_parts = clean_word.split('.')
                masked_ip = f"{ip_parts[0]}.{ip_parts[1]}.*.*"
                new_words.append(word.replace(clean_word, masked_ip))
            else:
                new_words.append(word)
        
        masked_logs.append(" ".join(new_words))
        
    print("Báo cáo log an toàn:")
    for idx, log in enumerate(masked_logs, 1):
        print(f"{idx}. {log}")
        
    return masked_logs

def main():
    while True:
        print("""============= SECURITY LOG ANALYZER =============
    1. Nhập và làm sạch dữ liệu Log thô
    2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
    3. Mã hóa địa chỉ IP (Masking)
    4. Đóng hệ thống
    =================================================""")
        choice = int(input("Chọn chức năng (1-4): "))
        match choice:
            case 1:
                add_data()
            case 2:
                filter_high_alerts()
            case 3:
                mask_ip_addresses()
            case 4:
                print("Kết thúc chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 4.")

if __name__ == "__main__":
    main()