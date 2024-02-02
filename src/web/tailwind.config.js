/*
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2024-02-02 17:50:59
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2024-02-02 20:16:44
 * @FilePath: /nexus/src/web/tailwind.config.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{svelte,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["luxury"],
  },
}

