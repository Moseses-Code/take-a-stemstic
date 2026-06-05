const API_URL = "http://127.0.0.1:8000";

export async function getStatistics(steamId) {
  const response = await fetch(
    `${API_URL}/statistics/${steamId}`
  );

  return response.json();
}

export async function getGames(steamId) {
  const response = await fetch(
    `${API_URL}/games/${steamId}`
  );

  return response.json();
}
export async function syncProfile(steamId) {
  const response = await fetch(
    `${API_URL}/sync/${steamId}`,
    {
      method: "POST",
    }
  );

  return response.json();
}
export async function getUser(steamId) {
  const response = await fetch(
    `${API_URL}/users/steam/${steamId}`
  );

  return response.json();
}