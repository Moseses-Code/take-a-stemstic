import { useEffect, useState } from "react";
import {
  getGames,
  getStatistics,
  syncProfile,
  getUser,
} from "../services/api";
import "./Dashboard.css";

const STEAM_ID = "76561199441718268";

function Dashboard() {
  const [statistics, setStatistics] = useState(null);
  const [games, setGames] = useState([]);
  const [user, setUser] = useState(null);
  const [isSyncing, setIsSyncing] = useState(false);

  async function loadData() {
  const statisticsData = await getStatistics(STEAM_ID);
  const gamesData = await getGames(STEAM_ID);
  const userData = await getUser(STEAM_ID);

  setStatistics(statisticsData);
  setGames(gamesData);
  setUser(userData);
}

  useEffect(() => {
    loadData();
  }, []);

  async function handleSync() {
    try {
      setIsSyncing(true);

      await syncProfile(STEAM_ID);
      await loadData();

      alert("Синхронизация завершена");
    } catch (error) {
      alert("Ошибка синхронизации");
      console.error(error);
    } finally {
      setIsSyncing(false);
    }
  }

  if (!statistics || !user) {
    return (
      <main className="dashboard-page">
        <section className="dashboard-content">
          <h1>Загрузка...</h1>
        </section>
      </main>
    );
  }

  const sortedGames = [...games]
    .sort((a, b) => b.hours - a.hours)
    .slice(0, 5);

  return (
    <main className="dashboard-page">
      <aside className="sidebar">
        <div className="sidebar-logo">📈 TaS</div>

        <nav className="sidebar-nav">
          <a className="active">Главная</a>
          <a>Игры</a>
          <a>Бэклог</a>
          <a>Статистика</a>
          <a>Настройки</a>
        </nav>
      </aside>

      <section className="dashboard-content">
        <header className="dashboard-header">
            <div className="profile-header">
                <img
                src={user.avatar_url}
                alt={user.nickname}
                className="profile-avatar"
                />

            <div>
                <p>Добро пожаловать</p>
                <h1>{user.nickname}</h1>

                <span className="profile-steamid">
                    Steam ID: {user.steam_id}
                </span>
                <span className="profile-level">
                    Steam Level: {user.steam_level}
                </span>
            </div>
        </div>

  <button onClick={handleSync} disabled={isSyncing}>
    {isSyncing ? "Синхронизация..." : "Синхронизировать"}
  </button>
</header>

        <section className="stats-grid">
          <div className="dashboard-card">
            <span>Всего игр</span>
            <strong>{statistics.total_games}</strong>
          </div>

          <div className="dashboard-card">
            <span>Всего часов</span>
            <strong>{statistics.total_hours}</strong>
          </div>

          <div className="dashboard-card">
            <span>Сыграно</span>
            <strong>{statistics.played_percent}%</strong>
          </div>

          <div className="dashboard-card">
            <span>Бэклог</span>
            <strong>{statistics.backlog_count}</strong>
          </div>
        </section>

        <section className="dashboard-main-grid">
          <div
            className="dashboard-panel favorite-panel"
            style={{
            backgroundImage: `
            linear-gradient(
            90deg,
          rgba(15, 23, 42, 0.95),
          rgba(15, 23, 42, 0.55)
            ),
            url(https://cdn.cloudflare.steamstatic.com/steam/apps/${statistics.favorite_game_appid}/header.jpg)
            `,
            }}
        >
            <span>⭐ Любимая игра</span>
            <h2>{statistics.favorite_game_name}</h2>
            <p>{statistics.favorite_game_hours} часов</p>
            </div>

          <div className="dashboard-panel">
            <h3>Топ игр из базы</h3>

            {sortedGames.map((game) => (
              <div className="game-row" key={game.steam_app_id}>
                <span>{game.name}</span>
                <strong>{game.hours} ч</strong>
              </div>
            ))}
          </div>
        </section>
      </section>
    </main>
  );
}

export default Dashboard;