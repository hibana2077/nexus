<script>
// @ts-nocheck
  import { writable } from 'svelte/store';
	import '@carbon/charts-svelte/styles.css';
  import AutoComplete from "simple-svelte-autocomplete";
  import Main from './lib/Main.svelte';
  import About from './lib/About.svelte';
  import Error from './lib/Error.svelte';
  import Find from './lib/Find.svelte';

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

{:else if $now_page === "about"}

<!-- about page  -->

<About />

{:else if $now_page === "find"}

<!-- find page  -->

<Find />

{:else}

<!-- 404 page  -->

<Error {changePage} />

{/if}