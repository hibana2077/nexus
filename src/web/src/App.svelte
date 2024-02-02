<script>
	import '@carbon/charts-svelte/styles.css'
	import { BarChartSimple, ChartTheme } from '@carbon/charts-svelte'
</script>

<div class="mt-4 mx-4">
  <div class="navbar bg-primary shadow-lg rounded-lg">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
        </div>
        <ul class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-primary rounded-box w-52">
          <li><a href="./">Homepage</a></li>
          <li><a href="./">Profile</a></li>
          <li><a href="./">About</a></li>
        </ul>
      </div>
    </div>
    <div class="navbar-center">
      <a class="btn btn-ghost text-xl" href="./">NEXUS</a>
    </div>
    <div class="navbar-end">
      <button class="btn btn-ghost btn-circle">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
      </button>
      <button class="btn btn-ghost btn-circle">
        <div class="indicator">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 512 512" stroke="currentColor"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M448 341.37V170.61A32 32 0 00432.11 143l-152-88.46a47.94 47.94 0 00-48.24 0L79.89 143A32 32 0 0064 170.61v170.76A32 32 0 0079.89 369l152 88.46a48 48 0 0048.24 0l152-88.46A32 32 0 00448 341.37z"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="32" d="M69 153.99l187 110 187-110M256 463.99v-200"/><ellipse cx="256" cy="152" rx="24" ry="16"/><ellipse cx="208" cy="296" rx="16" ry="24"/><ellipse cx="112" cy="328" rx="16" ry="24"/><ellipse cx="304" cy="296" rx="16" ry="24"/><ellipse cx="400" cy="240" rx="16" ry="24"/><ellipse cx="304" cy="384" rx="16" ry="24"/><ellipse cx="400" cy="328" rx="16" ry="24"/></svg>
        </div>
      </button>
    </div>
  </div>
</div>

<!-- mainpage  -->

<div class="flex mt-4 mx-4">
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center mr-2">
    content
  </div>
  <div class="grid h-80 flex-grow card bg-base-300 rounded-box place-items-center ml-2">content</div>
</div>

<div class="flex mt-4 mx-4 card bg-base-300 rounded-box">
  <BarChartSimple
  style="padding:2rem;"
	data={[
		{ group: 'Qty', value: 65000 },
		{ group: 'More', value: 29123 },
		{ group: 'Sold', value: 35213 },
		{ group: 'Restocking', value: 51213 },
		{ group: 'Misc', value: 16932 }
	]}
	options={{
		theme: ChartTheme.G100,
		title: 'Simple bar (discrete)',
		height: '500px',
		axes: {
			left: { mapsTo: 'value' },
			bottom: { mapsTo: 'group', scaleType: 'labels' }
		}
	}} />
</div>