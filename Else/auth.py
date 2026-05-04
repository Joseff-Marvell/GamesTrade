import pyrebase

# Параметри з проєкту Firebase
config = {
    "apiKey": "AIzaSyDHJYQO9BPPJLA5CHN3bM01r_xzBK6qLTM",
    "authDomain": "tradegames-bd064.firebaseapp.com",
    "projectId": "tradegames-bd064",
    "storageBucket": "tradegames-bd064.firebasestorage.app",
    "messagingSenderId": "975164534116",
    "appId": "1:975164534116:web:9828df851c1b152d7f9e71",
    "databaseURL": "" # Можна залишити порожнім, якщо не використовуєте Realtime DB
}

# Ініціалізація
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# --- ФУНКЦІЇ ---

def register(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Аккаунт створено успішно!")
    except Exception as e:
        print(f"Помилка реєстрації: {e}")

def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        # Отримуємо ID токен користувача
        id_token = user['idToken']
        print("Аутентфікація успішна!")
        return id_token
    except Exception as e:
        print(f"Помилка входу: {e}")
        return None

# Приклад використання
user_email = "nazarij.lvivlute@gmail.com"
user_pass = "lutelviv1"

# Викликати один раз для створення облікового запису, потім заглушити
# register(user_email, user_pass)
token = login(user_email, user_pass)
print(token)
