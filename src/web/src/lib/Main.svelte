<script>
    // @ts-nocheck
    import '@carbon/charts-svelte/styles.css';
    import { BarChartSimple, ChartTheme, LineChart } from '@carbon/charts-svelte';

    let stock_data = [
        { group: 'IX0001', value: 17590, date: "2018-12-31T16:00:00.000Z"},
        { group: 'IX0001', value: 17580, date: "2019-01-01T16:00:00.000Z"},
        { group: 'IX0001', value: 17590, date: "2019-01-02T16:00:00.000Z"},
        { group: 'IX0001', value: 17580, date: "2019-01-03T16:00:00.000Z"},
        { group: 'IX0001', value: 17586, date: "2019-01-04T16:00:00.000Z"},
        { group: 'IX0001', value: 17588, date: "2019-01-05T16:00:00.000Z"},
        { group: 'IX0001', value: 17530, date: "2019-01-06T16:00:00.000Z"},
        { group: 'IX0001', value: 17520, date: "2019-01-07T16:00:00.000Z"},
        { group: 'IX0001', value: 17510, date: "2019-01-08T16:00:00.000Z"},
        { group: 'IX0001', value: 17500, date: "2019-01-09T16:00:00.000Z"},
        { group: 'IX0001', value: 17490, date: "2019-01-10T16:00:00.000Z"},
        { group: 'IX0001', value: 17480, date: "2019-01-11T16:00:00.000Z"},
        { group: 'IX0001', value: 17470, date: "2019-01-12T16:00:00.000Z"},
        { group: 'IX0001', value: 17460, date: "2019-01-13T16:00:00.000Z"},
        { group: 'IX0001', value: 17450, date: "2019-01-14T16:00:00.000Z"},
        { group: 'IX0001', value: 17440, date: "2019-01-15T16:00:00.000Z"},
        { group: 'IX0186', value: 150.24, date: "2018-12-31T16:00:00.000Z"},
        { group: 'IX0186', value: 150.05, date: "2019-01-01T16:00:00.000Z"},
        { group: 'IX0186', value: 150.66, date: "2019-01-02T16:00:00.000Z"},
        { group: 'IX0186', value: 148.05, date: "2019-01-03T16:00:00.000Z"},
        { group: 'IX0186', value: 150.24, date: "2019-01-04T16:00:00.000Z"},
        { group: 'IX0186', value: 150.05, date: "2019-01-05T16:00:00.000Z"},
        { group: 'IX0186', value: 150.01, date: "2019-01-06T16:00:00.000Z"},
        { group: 'IX0186', value: 150.23, date: "2019-01-07T16:00:00.000Z"},
        { group: 'IX0186', value: 150.24, date: "2019-01-08T16:00:00.000Z"},
        { group: 'IX0186', value: 150.29, date: "2019-01-09T16:00:00.000Z"},
        { group: 'IX0186', value: 150.55, date: "2019-01-10T16:00:00.000Z"},
        { group: 'IX0186', value: 150.66, date: "2019-01-11T16:00:00.000Z"},
        { group: 'IX0186', value: 130.24, date: "2019-01-12T16:00:00.000Z"},
        { group: 'IX0186', value: 135.05, date: "2019-01-13T16:00:00.000Z"},
        { group: 'IX0186', value: 125.24, date: "2019-01-14T16:00:00.000Z"},
        { group: 'IX0186', value: 170.05, date: "2019-01-15T16:00:00.000Z"}
    ]
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
              <tr>
                <th></th>
                <td>Apple releases new iPhone</td>
                <td>Apple releases new iPhone, which is the most powerful iPhone ever</td>
                <td><a href="https://www.apple.com/iphone-13-pro/" target="_blank">Link</a></td>
              </tr>
              <!-- row 2 -->
              <tr>
                <th></th>
                <td>TSMC to build new factory in Japan</td>
                <td>Dr. C.C. Wei, CEO of TSMC, announced that TSMC will build a new factory in Japan</td>
                <td>Purple</td>
              </tr>
              <!-- row 3 -->
              <tr>
                <th></th>
                <td>Brice Swyre</td>
                <td>Tax Accountant</td>
                <td>Red</td>
              </tr>
              <tr>
                <th></th>
                <td>Brice Swyre</td>
                <td>Tax Accountant</td>
                <td>Red</td>
              </tr>
              <tr>
                <th></th>
                <td>Brice Swyre</td>
                <td>Tax Accountant</td>
                <td>Red</td>
              </tr>
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
            <iframe title="Stock Chart" frameBorder='0' scrolling='no' width='450' height='225' src='https://api.stockdio.com/visualization/financial/charts/v1/SingleQuote?app-key=8534C99CCADD4AFDB1D17BD809453DD7&stockExchange=TWSE&symbol=2409&showLogo=No&palette=Aurora&width=450px&height=225px'></iframe>
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
                    mapsTo: 'value',
                    title: 'Stock Price',
                    scaleType: 'log'
                }
            },
            curve: 'curveMonotoneX',
            height: '500px'
      }} />
</div>
  