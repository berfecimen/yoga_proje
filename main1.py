# Yorum sınıfı
class Comment:
    def __init__(self, user, content):
        # Yorumun sahibi (user) ve içeriği (content) ile başlatılır
        self.user = user
        self.content = content

    def display(self):
        # Yorum sahibinin kullanıcı adı ve yorum içeriğini ekrana yazdırır
        print(f"{self.user.username}: {self.content}")

# Kullanıcı sınıfı ve türevleri
class User:
    def __init__(self, username, email, password, role):
        # Kullanıcı adı, email, şifre ve rol bilgileri ile başlatılır
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.reservations = []  # Kullanıcının rezervasyon yaptığı yoga dersleri listesi
        self.comments = []  # Kullanıcının yaptığı yorumlar listesi

    def reserve_class(self, yoga_class):
        # Kullanıcı bir yoga dersine rezervasyon yapar
        if yoga_class.add_participant(self):
            # Eğer dersin kapasitesi müsaitse, rezervasyon yapılır ve kullanıcıya eklenir
            self.reservations.append(yoga_class)
            print(f"{self.username} reserved a spot in {yoga_class.name}")
        else:
            # Kapasite doluysa rezervasyon yapılamaz
            print(f"Reservation failed for {yoga_class.name}")

    def receive_notification(self, notification):
        # Kullanıcıya bildirim gönderir
        print(f"Notification for {self.username}: {notification}")

    def add_comment(self, yoga_class, content):
        # Kullanıcı bir yoga dersine yorum ekler
        comment = Comment(self, content)
        yoga_class.add_comment(comment)

class Student(User):
    def __init__(self, username, email, password):
        # Student sınıfı, User sınıfından türetilir ve rolü "Student" olarak ayarlanır
        super().__init__(username, email, password, "Student")

class Instructor(User):
    def __init__(self, username, email, password):
        # Instructor sınıfı, User sınıfından türetilir ve rolü "Instructor" olarak ayarlanır
        super().__init__(username, email, password, "Instructor")

# Yoga dersi sınıfı
class YogaClass:
    def __init__(self, name, instructor, date, time, capacity):
        # Yoga dersinin adı, eğitmeni, tarihi, saati ve kapasitesi ile başlatılır
        self.name = name
        self.instructor = instructor
        self.date = date
        self.time = time
        self.capacity = capacity
        self.participants = []  # Dersin katılımcıları listesi
        self.comments = []  # Ders için yapılan yorumlar listesi

    def add_participant(self, participant):
        # Dersin kapasitesine bağlı olarak katılımcı ekler
        if len(self.participants) < self.capacity:
            # Kapasite uygun ise katılımcı eklenir
            self.participants.append(participant)
            return True
        # Kapasite dolu ise katılımcı eklenemez
        return False

    def notify_participants(self, message):
        # Tüm katılımcılara bildirim gönderir
        for participant in self.participants:
            participant.receive_notification(message)

    def display_info(self):
        # Dersin bilgilerini ekrana yazdırır
        print(f"{self.name} by {self.instructor.username} on {self.date} at {self.time} (Capacity: {self.capacity - len(self.participants)}/{self.capacity})")

    def add_comment(self, comment):
        # Derse yorum ekler
        self.comments.append(comment)

    def display_comments(self):
        # Dersin yorumlarını ekrana yazdırır
        print(f"Comments for {self.name}:")
        for comment in self.comments:
            comment.display()

# Ders programı sınıfı
class Schedule:
    def __init__(self):
        # Programdaki yoga dersleri listesi
        self.classes = []

    def add_class(self, yoga_class):
        # Programa yoga dersi ekler
        self.classes.append(yoga_class)

    def display_schedule(self):
        # Programdaki tüm dersleri ekrana yazdırır
        for yoga_class in self.classes:
            yoga_class.display_info()

# Kullanıcı ve ders ekleme fonksiyonları
def add_user(users, user):
    # Kullanıcı listesine yeni kullanıcı ekler
    users.append(user)

def add_class(schedule, yoga_class):
    # Ders programına yeni ders ekler
    schedule.add_class(yoga_class)

def find_class_by_name(schedule, name):
    # Ders programında isme göre ders arar
    for yoga_class in schedule.classes:
        if yoga_class.name == name:
            return yoga_class
    return None

def display_classes(schedule):
    # Ders programını ekrana yazdırır
    schedule.display_schedule()

# Yoga bilgisi görüntüleme fonksiyonu
def display_yoga_info():
    # Yoga hakkında bilgi metnini ekrana yazdırır
    yoga_info = """
    Yoga Nedir?

    Yoga, Hindistan kökenli bir felsefe ve yaşam pratiğidir. Fiziksel duruşlar (asana), nefes teknikleri (pranayama) ve meditasyonu birleştirerek beden ve zihin arasındaki uyumu sağlar. Modern dünyada hem fiziksel sağlık hem de zihinsel rahatlama için yaygın olarak uygulanmaktadır.

    Ne işe yarar?
    Yoga, vücudu esnekleştirir, kasları güçlendirir ve duruş bozukluklarını düzeltir. Düzenli pratikle stres seviyesini azaltır, zihni sakinleştirir ve odaklanmayı artırır. Ayrıca, uyku kalitesini iyileştirebilir ve genel yaşam enerjisini yükseltebilir.

    Vinyasa Yoga: Nefes ve hareketin senkronize bir şekilde aktığı, pozların belli bir temaya göre sıralandığı bir yoga stilidir.

    Hatha Yoga: Temel yoga stilidir ve pozlar detaylı hiza bilgileriyle derinlemesine incelenir.

    Ashtanga Yoga: Yoga’nın sekiz kolunu temsil eden, belirli bir seriyi nefes ve hareketle birleştiren bir yoga stilidir. Sekiz kol; dış (yama, niyama, asana, pranayama) ve iç kollar (pratyahara, dharana, dhyana, samadhi) olarak ikiye ayrılır.

    Yin Yoga: Pozların yerde ve pasif bir şekilde daha uzun süre hareketsiz uygulandığı bir yoga türüdür. Bağ dokuların esnekliğini artırmayı hedefler.

    Restoratif Yoga: Vücudu malzemelerle destekleyerek derin dinlenme ve yenilenme sağlayan bir yoga stilidir.

    Kundalini Yoga: Pozlar ve yoğun nefes çalışmalarını birleştirerek farkındalık kazandırmayı amaçlar.

    Hamile Yogası: Rahat bir hamilelik süreci ve doğum için bedensel esneklik ve doğru nefes kontrolüne odaklanır.

    Çocuk Yogası: Çocukların beden koordinasyonu, esneklik ve konsantrasyonlarını geliştiren bir yoga stilidir.

    Hamak Yogası: Kumaş hamaklar yardımıyla yapılan, vücuda destek sağlayarak yer çekimine karşı çalışmayı kolaylaştıran bir yoga stilidir. Esnekliği artırırken kasları güçlendirir ve omurga üzerindeki baskıyı azaltır. Aynı zamanda farklı bir perspektif sunarak zihinsel rahatlama sağlar.
    """
    print(yoga_info)

# Kullanıcı kayıt ve giriş fonksiyonları
def register_user(users):
    # Kullanıcı kayıt işlemi
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    role = input("Enter role (Student/Instructor): ")

    if role.lower() == "student":
        user = Student(username, email, password)
    elif role.lower() == "instructor":
        user = Instructor(username, email, password)
    else:
        print("Invalid role!")
        return

    add_user(users, user)
    print(f"User {username} registered successfully!")

def login_user(users):
    # Kullanıcı giriş işlemi
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.username == username and user.password == password:
            print(f"Welcome, {username}!")
            return user

    print("Invalid username or password!")
    return None

# Ana program döngüsü
def main():
    users = []  # Kullanıcı listesi
    schedule = Schedule()  # Yoga ders programı

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. What is Yoga?")  # Yoga bilgisi görüntüleme seçeneği eklendi
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user(users)
        elif choice == "2":
            user = login_user(users)
            if user:
                while True:
                    print("\n1. Reserve Class")
                    print("2. View Classes")
                    print("3. Add Comment")
                    print("4. View Comments")
                    if user.role == "Instructor":
                        print("5. Add Class")
                    print("6. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        display_classes(schedule)
                        class_name = input("Enter class name to reserve: ")
                        yoga_class = find_class_by_name(schedule, class_name)
                        if yoga_class:
                            user.reserve_class(yoga_class)
                        else:
                            print("Class not found!")
                    elif user_choice == "2":
                        display_classes(schedule)
                    elif user_choice == "3":
                        display_classes(schedule)
                        class_name = input("Enter class name to comment on: ")
                        yoga_class = find_class_by_name(schedule, class_name)
                        if yoga_class:
                            content = input("Enter your comment: ")
                            user.add_comment(yoga_class, content)
                        else:
                            print("Class not found!")
                    elif user_choice == "4":
                        display_classes(schedule)
                        class_name = input("Enter class name to view comments: ")
                        yoga_class = find_class_by_name(schedule, class_name)
                        if yoga_class:
                            yoga_class.display_comments()
                        else:
                            print("Class not found!")
                    elif user_choice == "5" and user.role == "Instructor":
                        print("Select Yoga Type:")
                        print("1. Vinyasa Yoga")
                        print("2. Hatha Yoga")
                        print("3. Kundalini Yoga")
                        print("4. Hamak Yoga")
                        type_choice = input("Choose a type: ")
                        yoga_types = {
                            "1": "Vinyasa Yoga",
                            "2": "Hatha Yoga",
                            "3": "Kundalini Yoga",
                            "4": "Hamak Yoga"
                        }
                        if type_choice in yoga_types:
                            class_name = yoga_types[type_choice]
                            date = input("Enter date (YYYY-MM-DD): ")
                            time = input("Enter time (HH:MM): ")
                            capacity = int(input("Enter capacity: "))
                            yoga_class = YogaClass(class_name, user, date, time, capacity)
                            add_class(schedule, yoga_class)
                            print(f"{class_name} class added successfully!")
                        else:
                            print("Invalid type!")
                    elif user_choice == "6":
                        break
                    else:
                        print("Invalid option!")
        elif choice == "3":
            display_yoga_info()
        elif choice == "4":
            break
        else:
            print("Invalid option!")

if __name__ == '__main__':
    main()
