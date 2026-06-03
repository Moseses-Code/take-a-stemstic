import "./App.css";

function App() {
  return (
    <main className="page">
      <header className="header">
        <div className="logo">📈 Take-a-Steamstic</div>

        <nav className="nav">
          <a>Главная</a>
          <a>Возможности</a>
          <a>Пример статистики</a>
          <a>FAQ</a>
        </nav>

        <button className="steam-button">Войти через Steam</button>
      </header>

      <section className="hero">
        <div className="hero-content">
          <div className="badge">● Аналитика твоего Steam в одном месте</div>

          <h1>
            Узнай всё о своей игровой истории в <span>Steam</span>
          </h1>

          <p>
            Take-a-Steamstic помогает тебе понять свою игровую историю:
            сколько ты играешь, во что играешь и сколько всего ещё впереди.
          </p>

          <button className="main-button">Войти через Steam</button>

          <small>🔒 Мы не получаем доступ к вашему паролю.</small>
        </div>

        <div className="preview-placeholder">
          <div className="placeholder-content">
            <h2>Профиль пользователя</h2>

            <p>
              Здесь будет интерактивный скриншот профиля пользователя после
              завершения разработки панели управления.
            </p>

            <span>PREVIEW COMING SOON</span>
          </div>
        </div>
      </section>

      <section className="features">
        <h2>Что ты получишь</h2>

        <div className="feature-grid">
          <Feature
            icon="🎮"
            title="Полная статистика"
            text="Узнай, сколько часов ты играешь и как менялись твои игровые привычки."
          />

          <Feature
            icon="📦"
            title="Бэклог под контролем"
            text="Увидь игры, которые ты ещё не запускал или почти не проходил."
          />

          <Feature
            icon="⏱"
            title="Любимые игры"
            text="Найди свои топы по времени, активности и интересу."
          />

          <Feature
            icon="🏆"
            title="Достижения"
            text="В будущем добавим анализ достижений и прогресса."
          />
        </div>
      </section>
    </main>
  );
}

function Feature({ icon, title, text }) {
  return (
    <article className="feature-card">
      <div className="feature-icon">{icon}</div>
      <h3>{title}</h3>
      <p>{text}</p>
    </article>
  );
}

export default App;