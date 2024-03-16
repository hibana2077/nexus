<!--
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2024-02-02 17:40:31
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2024-02-20 17:19:43
 * @FilePath: /nexus/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<p align="center">
  <img src="./NEXUS.png" alt="NEXUS" width="200" />
</p>

<h1 align="center">NEXUS</h1>

![Svelte](https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 介紹

NEXUS 是一個使用 Svelte 3 + Tailwind CSS + Vite + FastAPI + Docker 開發的 Web App。</br>
透過選擇股票產業類別、輸入一些偏好條件，可以找到符合條件的潛力股票。</br>

## 功能

- [x] 熱門新聞
- [x] 熱門股票
- [x] 單一股票查詢
- [x] 按條件篩選股票
- [x] 即時股價(K線圖)
- [x] 個股資訊

## 安裝

- [Demo](###Demo)
- [本地安裝](###本地安裝)

### Demo

[Demo](http://nexus.hibana2077.com/)

NEXUS 目前部署在台東大學的某間實驗室的電腦。

### 本地安裝

1. 下載專案

```bash
git clone https://github.com/hibana2077/nexus.git
```

2. 安裝前端

```bash
cd nexus/src/web
npm install
```

3. 安裝後端

```bash
cd nexus/src/api
pip install -r requirements.txt
```

4. 啟動專案

```bash
cd nexus
cd src/api
uvicorn main:app --host 0.0.0.0 --port 8000
cd ../web
npm run dev -- --host
```

## Screenshot

<p align="center">

![Main](https://media.discordapp.net/attachments/956596033163505684/1204081787077263360/image.png?ex=65d36f8c&is=65c0fa8c&hm=eaca1474cf3f1e5491ba8a38851990df6cd2967125eb67296a837b9c7325f38b&=&format=webp&quality=lossless&width=603&height=468)

![Filter](https://media.discordapp.net/attachments/956596033163505684/1204082066745069679/image.png?ex=65d36fcf&is=65c0facf&hm=715e434feec2a401ea6a9c8ae78c5ae0960f6f01a0227ea8c2c71cf8f2640e88&=&format=webp&quality=lossless&width=342&height=468)

![Result1](https://media.discordapp.net/attachments/956596033163505684/1204082233191960596/image.png?ex=65d36ff7&is=65c0faf7&hm=4a7421402e103d8d2ced19996cdef6a09837be43e548df2e9bfde43bfcfbbb0d&=&format=webp&quality=lossless)

![Result2](https://media.discordapp.net/attachments/956596033163505684/1204082389673058324/image.png?ex=65d3701c&is=65c0fb1c&hm=373749169f01fb6b9710ddca3886ba61d0364770a221c5368e5d38f9d23aba05&=&format=webp&quality=lossless)

![Result3](https://media.discordapp.net/attachments/956596033163505684/1204082526654562385/image.png?ex=65d3703d&is=65c0fb3d&hm=0e244c4015e69ffe401c50c2f7db80250639486479e5f262ccea8a51367ce1e8&=&format=webp&quality=lossless&width=840&height=468)

</p>

## License

![GitHub](https://img.shields.io/github/license/hibana2077/nexus?style=for-the-badge)
