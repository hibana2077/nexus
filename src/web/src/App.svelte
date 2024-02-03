<script>
// @ts-nocheck
  import { writable } from 'svelte/store';
	import '@carbon/charts-svelte/styles.css';
  import AutoComplete from "simple-svelte-autocomplete";
  import Main from './lib/Main.svelte';

  const stocks_nums = ["0050", "00878", "2330", "0051"]
  let selectedStock = writable("")
  let click_search = false
  let now_page = writable("home");

  function changePage(page) {
    now_page.set(page);
  }
</script>

<div class="mt-4 mx-4">
  <div class="navbar bg-primary shadow-lg rounded-lg">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
        </div>
        <ul class="menu menu-sm dropdown-content mt-3 z-[40] p-2 shadow bg-primary rounded-box w-52">
          <li><a href="javascript:void(0)" on:click={() => changePage("home")}>Home</a></li>
          <li><a href="javascript:void(0)" on:click={() => changePage("find")}>Find</a></li>
          <li><a href="javascript:void(0)" on:click={() => changePage("profile")}>Profile</a></li>
          <li><a href="javascript:void(0)" on:click={() => changePage("about")}>About</a></li>
        </ul>
      </div>
    </div>
    <div class="navbar-center">
      <a class="btn btn-ghost text-xl" href="./">NEXUS</a>
    </div>
    <div class="navbar-end">
      <button class="btn btn-ghost btn-circle" on:click={() => click_search = !click_search}>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
      </button>
      {#if click_search}
        <div class="join">
          <div>
            <div>
              <AutoComplete items="{stocks_nums}" bind:selectedItem="{selectedStock}" class="input join-item"/>
            </div>
          </div>
          <select class="select select-bordered join-item">
            <option disabled selected>Filter</option>
            <option>Stock</option>
            <option>ETF</option>
            <option>Warrant</option>
          </select>
          <div class="indicator">
            <button class="btn join-item">Search</button>
          </div>
        </div>
      {/if}
      <button class="btn btn-ghost btn-circle">
        <div class="indicator">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 512 512" stroke="currentColor"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M448 341.37V170.61A32 32 0 00432.11 143l-152-88.46a47.94 47.94 0 00-48.24 0L79.89 143A32 32 0 0064 170.61v170.76A32 32 0 0079.89 369l152 88.46a48 48 0 0048.24 0l152-88.46A32 32 0 00448 341.37z"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M69 153.99l187 110 187-110M256 463.99v-200"/><ellipse cx="256" cy="152" rx="24" ry="16"/><ellipse cx="208" cy="296" rx="16" ry="24"/><ellipse cx="112" cy="328" rx="16" ry="24"/><ellipse cx="304" cy="296" rx="16" ry="24"/><ellipse cx="400" cy="240" rx="16" ry="24"/><ellipse cx="304" cy="384" rx="16" ry="24"/><ellipse cx="400" cy="328" rx="16" ry="24"/></svg>
        </div>
      </button>
    </div>
  </div>
</div>

{#if $now_page === "home"}

<!-- mainpage  -->

<Main />

{:else if $now_page === "profile"}

<!-- profile page  -->

<div class="flex mt-4 mx-4">
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center mr-2">
    content
  </div>
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center mr-2 ml-2">
    content
  </div>
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center ml-2">
    content
  </div>
</div>
<div class="flex mt-4 mx-4">
  <div class="grid h-40 flex-grow card bg-base-300 rounded-box place-items-center mr-2">
    content
  </div>
</div>


{:else if $now_page === "about"}

<!-- about page  -->

<div class="grid justify-items-center mt-8">
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center p-4 transition ease-in-out delay-150 hover:bg-primary hover:-translate-y-1 hover:scale-110 duration-300">
    <h1 class="text-4xl my-4">
      <strong>
        About Author
      </strong>
    </h1>
    <div class="avatar">
      <div class="w-32 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
        <img src="https://avatars.githubusercontent.com/u/72302793?size=128" alt="avatar" />
      </div>
    </div>
    <div class="text-center">
      <h2 class="text-2xl my-4">
        <strong>
          <a href="https://github.com/hibana2077" target="_blank">
            hibana2077
          </a>
        </strong>
      </h2>
    </div>
  </div>
</div>

<div class="mx-auto w-96 mt-8 bg-base-300 p-4 rounded-box shadow-xl">
  <div class="card w-90 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">Like this App?</h2>
      <p>You can go to my github and give me a star!</p>
      <div class="card-actions justify-end">
        <button class="btn btn-primary">
          <a href="https://www.github.com/hibana2077/nexus" target="_blank">Go to Github</a>
        </button>
      </div>
    </div>
  </div>
</div>

<div class="mx-auto w-96 mt-8 bg-base-300 p-4 rounded-box shadow-xl">
  <div class="card w-90 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">免責聲明</h2>
      <p>本應用程式提供的所有資訊僅供參考，不應被視為專業的投資建議。在作出任何投資決定前，用戶應進行獨立評估並可考慮尋求專業意見。本應用程式及其開發者對於任何用戶因依賴該等資訊所可能遭受的損失或損害不承擔任何責任。</p>
    </div>
  </div>
</div>

{:else if $now_page === "find"}

<!-- find page  -->

<div class="flex mt-4 mx-4">
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center mr-2">
    content
  </div>
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center ml-2">content</div>
</div>

{:else}

<!-- 404 page  -->

<div class="grid justify-items-center mt-8">
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center p-4 transition ease-in-out delay-150 hover:bg-primary hover:-translate-y-1 hover:scale-110 duration-300">
    <h1 class="text-4xl my-4">
      <strong>
        404
      </strong>
    </h1>
    <div class="text-center">
      <h2 class="text-2xl my-4">
        <strong>
          <a href="javascript:void(0)" on:click={() => changePage("home")}>
            Go back to home
          </a>
        </strong>
      </h2>
    </div>
  </div>
</div>

{/if}