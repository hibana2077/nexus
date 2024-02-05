<script>
  // @ts-nocheck
  import '@carbon/charts-svelte/styles.css';
  import { ChartTheme, LineChart } from '@carbon/charts-svelte';

  let stock_data;
  async function get_data() {
      try {
          const res = await fetch('http://0.0.0.0:8000/mainpage/indexprice', {
              method: 'GET'
          });

          if (!res.ok) {
              throw new Error(`HTTP error! status: ${res.status}`);
          }

          stock_data = await res.json();  // 直接將響應轉換為 JSON
      } catch (error) {
          console.error('Error fetching data: ', error);
      }
  }
  let hotstock;
  let top1;
  async function get_hotstock() {
      try {
          const res = await fetch('http://0.0.0.0:8000/hotstock', {
              method: 'GET'
          });

          if (!res.ok) {
              throw new Error(`HTTP error! status: ${res.status}`);
          }

          hotstock = await res.json();  // 直接將響應轉換為 JSON
          top1 = hotstock[0]['symbol'];
      } catch (error) {
          console.error('Error fetching data: ', error);
      }
  }

  let news;
  async function get_news() {
      try {
          const res = await fetch('http://0.0.0.0:8000/news', {
              method: 'GET'
          });

          if (!res.ok) {
              throw new Error(`HTTP error! status: ${res.status}`);
          }

          news = await res.json();  // 直接將響應轉換為 JSON
      } catch (error) {
          console.error('Error fetching data: ', error);
      }
  }

  get_news();
  get_hotstock();
  get_data();
</script>

<div class="flex my-4 mx-4">
    <div class="grid h-100 flex-grow card bg-base-300 rounded-box place-items-center mr-2">
        <h2 class="text-2xl my-4">
            <div class="tooltip" data-tip="Market Trend">
                <strong>
                    市場動態
                </strong>
            </div>
        </h2>
        <table class="table table-zebra table-pin-rows">
            <!-- head -->
            <thead>
              <tr>
                <th></th>
                <th>Title</th>
                <th>Abstract</th>
                <th>Link</th>
              </tr>
            </thead>
            <tbody>
              <!-- row 1 -->
              <!-- <tr>
                <th></th>
                <td>Apple releases new iPhone</td>
                <td>Apple releases new iPhone, which is the most powerful iPhone ever</td>
                <td><a href="https://www.apple.com/iphone-13-pro/" target="_blank">Link</a></td>
              </tr> -->
              {#if news}
                {#each news as item}
                  <tr>
                    <th></th>
                    <td>{item.title}</td>
                    <td>fake abs</td>
                    <td><a href={item.link} target="_blank">Link</a></td>
                  </tr>
                {/each}
              {:else}
                <p>Loading...</p>
              {/if}
            </tbody>
          </table>
          <div class="flex join p-2">
            <button class="join-item btn">«</button>
            <button class="join-item btn">Page 1</button>
            <button class="join-item btn">»</button>
          </div>
    </div>
    <div class="grid h-100 flex-grow card bg-base-300 rounded-box place-items-center ml-2">
        <h2 class="text-2xl">
            <div class="tooltip" data-tip="Hot Stocks">
                <strong>
                    熱門股票
                </strong>
            </div>
        </h2>
        <div class="flex items-start">
            {#if top1}
              <iframe title="Stock Chart" frameBorder='0' scrolling='no' width='450' height='225' src='https://api.stockdio.com/visualization/financial/charts/v1/SingleQuote?app-key=8534C99CCADD4AFDB1D17BD809453DD7&stockExchange=TWSE&symbol={top1}&showLogo=No&palette=Aurora&width=450px&height=225px'></iframe>
            {:else}
              <p>Loading...</p>
            {/if}
        </div>
    </div>
  </div>
  
  <div class="flex mt-4 mx-4 card bg-base-300 rounded-box">
    <!-- <BarChartSimple
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
      }} /> -->
    {#if stock_data}
      <LineChart
      style="padding:2rem;"
        data={stock_data}
        options={{
              theme: ChartTheme.G100,
              title: 'Stock Price',
              axes: {
                  bottom: {
                      title: 'Time',
                      mapsTo: 'date',
                      scaleType: 'time'
                  },
                  left: {
                      mapsTo: 'close',
                      title: 'Stock Price',
                      scaleType: 'log'
                  }
              },
              curve: 'curveMonotoneX',
              height: '500px'
        }} />
    {:else}
      <p>Loading...</p>
    {/if}
</div>
  