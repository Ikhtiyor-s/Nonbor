<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NonBor Qo‘llanma</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background: #f5f5f5;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 600px;
      margin: auto;
      padding: 20px;
    }
    img.logo {
      width: 150px;
      margin: 20px auto;
      display: block;
    }
    h2 {
      margin-top: 25px;
      font-size: 22px;
      color: #333;
    }
    .btn {
      display: block;
      margin: 10px auto;
      padding: 14px;
      width: 90%;
      border-radius: 10px;
      text-decoration: none;
      font-weight: bold;
      box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
      transition: transform 0.2s, opacity 0.2s;
    }
    .btn:hover {
      transform: scale(1.02);
      opacity: 0.9;
    }
    .pdf { background: #dc3545; color: #fff; }
    .video { background: #007bff; color: #fff; }
    .store-container {
      display: flex;
      justify-content: space-between;
      margin-top: 20px;
      gap: 10px;
    }
    .store-box {
      flex: 1;
      background: #fff;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    .store-box img {
      width: 120px;
      margin-bottom: 10px;
    }
    .store-box a {
      display: block;
      margin: 5px 0;
      padding: 10px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: bold;
      color: #fff;
      background: #28a745;
    }
    .contact {
      margin-top: 25px;
      background: #FF6833;
      color: black;
      padding: 15px;
      border-radius: 10px;
      display: inline-block;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Logotip -->
    <img src="nonbor_logo.png" alt="NonBor Logo" class="logo">

    <!-- Sotuvchi qo‘llanmasi -->
    <h2>📘 Sotuvchi qo‘llanmasi</h2>
    <a class="btn pdf" href="merchant ru.pdf" target="_blank">📑 PDF qo‘llanma</a>
    <a class="btn video" href="https://example.com/sotuvchi_video.mp4" target="_blank">🎬 Video qo‘llanma</a>

    <!-- Mijoz qo‘llanmasi -->
    <h2>📘 Mijoz qo‘llanmasi</h2>
    <a class="btn pdf" href="https://example.com/nonbor_mijoz.pdf" target="_blank">📑 PDF qo‘llanma</a>
    <a class="btn video" href="https://example.com/mijoz_video.mp4" target="_blank">🎬 Video qo‘llanma</a>

    <!-- Yuklab olish bo‘limi -->
    <h2>⬇️ Ilovani yuklab olish</h2>
    <div class="store-container">
      <!-- App Store -->
      <div class="store-box">
        <img src="appstore.png" alt="App Store">
        <a href="https://apps.apple.com/uz/app/nonbor-business/id6743842538">📱 Sotuvchi ilova</a>
        <a href="https://apps.apple.com/uz/app/nonbor/id6743315956">📱 Mijoz ilova</a>
      </div>
      <!-- Play Market -->
      <div class="store-box">
        <img src="playmarket.png" alt="Play Market">
        <a href="https://play.google.com/store/apps/details?id=uz.welltech.nonborbusiness&hl=ru" target="_blank">📱 Sotuvchi ilova</a>
        <a href="https://play.google.com/store/apps/details?id=uz.welltech.nonbor.nonboruz&hl=ru">📱 Mijoz ilova</a>
      </div>
    </div>

    <!-- Murojaat -->
    <a class="contact" href="tel:+998948679300">📲 Murojaat qilish</a>
  </div>
</body>
</html>

