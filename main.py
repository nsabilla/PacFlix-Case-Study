from tabulate import tabulate 

class User:
    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan
        
    def check_all_plan(self):
        """
        Function untuk menampilkan all plan dari PacFlix
        """
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]
        
        table = [
            [True, True, True, "Bisa Stream"],
            [True, True, True, "Bisa Download"],
            [True, True, True, "Kualitas SD"],
            [False, True, True, "Kualitas HD"],
            [False, False, True, "Kualitas UHD"],
            [1, 2, 4, "Number of Devices"],
            ["3rd Party Movie", "Basic Plan + Sports", "Basic + Standard Plan + PacFlix Original", "Konten"],
            [120_000, 160_000, 200_000, "Harga"]
        ]
        
        print("All PacFlix Subs List")
        print("")
        print(tabulate(table, headers = headers, tablefmt="github"))
        
    def check_plan(self, username):
        """
        Function untuk menampilkan plan yang dimiliki oleh user
        
        Parameters
        ----------
        username: string
            input username
        """
        for key, value in data.items():
            
            if self.username == key:
                print(f"Username: {key}")
                print(f"Plan: {value[0]}")
                print(f"Duration plan: {value[1]}")
                
                try:
                    if value[0] == "Basic Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [False, "Kualitas HD"],
                         [False, "Kualitas UHD"],
                         [1, "Number of Devices"],
                         ["3rd party Movie only", "Jenis Konten"],
                         [120_000, "Harga"]]

                        headers = ["Basic Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))
                        
                    elif value[0] == "Standard Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [True, "Kualitas HD"],
                         [False, "Kualitas UHD"],
                         [2, "Number of Devices"],
                         ["Basic + Sports", "Jenis Konten"],
                         [160_000, "Harga"]]

                        headers = ["Standard Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))
                        
                    elif value[0] == "Premium Plan":
                        table = [[True, "Bisa Stream"],
                         [True, "Bisa Download"],
                         [True, "Kualitas SD"],
                         [True, "Kualitas HD"],
                         [True, "Kualitas UHD"],
                         [4, "Number of Devices"],
                         ["Basic + Standard Plan + PacFlix Original", "Jenis Konten"],
                         [200_000, "Harga"]]

                        headers = ["Premium Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers))
                        
                    else:
                        raise Exception("Plan tidak tersedia")
                        
                except:
                    raise Exception("Program tidak sesuai dengan ketentuan")
                    
    def upgrade_plan(self, current_plan, upgrade_plan):
        """
        Function untuk menghitung harga akhir jika user Upgrade Plan
        dan akan dapat diskon jika duration plan > 12
        
        Parameters
        ----------
        current_plan: string
            plan yang dimiliki existing user
            
        upgrade_plan: string
            new plan yang dipilih oleh user
            
        Returns
        -------
        total: float
            final price yang harus dibayar user
        """
        if upgrade_plan != current_plan:
            
            if self.duration_plan > 12:
                
                if upgrade_plan == "Basic Plan":
                    total = 120_000 - (120_000 * 0.05)
                    return total
                
                elif upgrade_plan == "Standard Plan":
                    total = 160_000 - (160_000 * 0.05)
                    return total
                
                elif upgrade_plan == "Premium Plan":
                    total = 200_000 - (200_000 * 0.05)
                    return total
                
                else:
                    raise Exception("Upgrade plan tidak ada")
                    
            else:
                
                if upgrade_plan == "Basic Plan":
                    total = 120_000
                    return total
                
                elif upgrade_plan == "Standard Plan":
                    total = 160_000
                    return total
                
                elif upgrade_plan == "Premium Plan":
                    total = 200_000
                    return total
                
                else:
                    raise Exception("Upgrade plan tidak ada")
                    
        else:
            raise Exception("Plan yang dipilih masih sama")
        
# isi titik - titik di bawah ini
class NewUser:
    
    existing_referral_code = []
    
    def __init__(self, username):
        self.username = username
        
    def get_referral_code(self, data):
        """
        Function untuk mendapatkan referral code dari database
        
        Parameters
        ----------
        data: dictionary
            database existing user PacFlix
            
        Returns
        -------
        existing_referral_code: list
            list referral code yang ada di database
        """
        for value in data.values():
            ref_code = value[2]
            self.existing_referral_code.append(ref_code)
            
        return self.existing_referral_code
    
    def pick_plan(self, new_plan, referral_code):
        """
        Function untuk menghitung final price dari new user
        akan dapat diskon 4% jika menggunakan referral code yang valid
        
        Parameters
        ----------
        new_plan: string
            plan yang dipilih user baru
            
        referral_code: string
            referral code yang diinput oleh user
            
        Returns
        -------
        total: float
            total akhir yang harus dibayar oleh user
        """
        if referral_code in self.existing_referral_code:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * 0.04)
                return total
            
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * 0.04)
                return total
            
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * 0.04)
                return total
            
            else:
                raise Exception("Plan yang dipilih tidak ada")
            
        else:
            raise Exception("Referral Code tidak valid!")


data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

user_1 = User(username = "Shandy",
              duration_plan = 12,
              current_plan = "Premium Plan")

print(user_1.check_all_plan())