import { Link, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import "./App.css";

function Landing() {
  function handlePreviewMove(event) {
    const card = event.currentTarget;
    const rect = card.getBoundingClientRect();

    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = ((y - centerY) / centerY) * -8;
    const rotateY = ((x - centerX) / centerX) * 8;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
  }

  function handlePreviewLeave(event) {
    const card = event.currentTarget;

    card.style.transform =
      "perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)";
  }

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

        <Link to="/dashboard" className="steam-button">
          Войти через Steam
        </Link>
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

          <Link to="/dashboard" className="main-button">
            Войти через Steam
          </Link>

          <small>🔒 Мы не получаем доступ к вашему паролю.</small>
        </div>

        <div
          className="preview-placeholder"
          onMouseMove={handlePreviewMove}
          onMouseLeave={handlePreviewLeave}
        >
          <div className="placeholder-content">
            <div className="preview-window">
              <div className="preview-window-header">
                <span></span>
                <span></span>
                <span></span>
              </div>

              <div className="preview-skeleton">
                <div className="skeleton-avatar"></div>

                <div className="skeleton-lines">
                  <div></div>
                  <div></div>
                </div>
              </div>

              <div className="skeleton-grid">
                <div></div>
                <div></div>
                <div></div>
              </div>
            </div>

            <span className="preview-text">
              Ваш профиль Steam появится здесь
            </span>
          </div>
        </div>
      </section>

      <section className="ad-section">
        <div className="ad-banner">
          <div className="ad-label">Реклама</div>

          <div className="ad-content">
            <h3>Здесь может быть ваш баннер</h3>

            <p>
              Поддержите развитие Take-a-Steamstic и расскажите о своём продукте
              тысячам игроков Steam.
            </p>

            <button>Подробнее</button>
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

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
}

export default App;