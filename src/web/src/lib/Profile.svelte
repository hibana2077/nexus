<script>
  import { writable } from "svelte/store";

  export let stock_id = 'ID';
  export let dialog_id = 'no-name';
  export let stock_name = '台積電';
  export let dividend = "5";
  export let safety = "0.8";

  // need to connect to api to get data
  const url = 'http://0.0.0.0:8000/profile/singlestock';
  let stock_detail = writable({
    bookValue_evaulate: "Loading",
    dividend_evaulate: "Loading",
    bookValue: "Loading",
    fair_price: "Loading"
  });
  let search_done = false;

  function getStockDetail() {
    search_done = false;
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        stock: stock_id,
        dividend_rate: dividend,
        safety: safety
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log("Data received:", data); // 檢查接收到的數據
      stock_detail.set(data);
      search_done = true;
    })
    .catch((error) => {
      console.error('Error:', error);
      // 可能您需要在這裡處理錯誤，例如通過設置某個狀態或顯示錯誤消息
    });
  }


  $: getStockDetail();
</script>

<dialog id={dialog_id} class="modal">
    <div class="modal-box w-11/12 max-w-7xl">
      <h2 class="font-bold text-2xl text-center my-2">
        <a href="https://www.fugle.tw/ai/{stock_id}" target="_blank" class="tooltip" data-tip="前往購買">
        {stock_id} - {stock_name}
        </a>
      </h2>
      <div class="grid grid-cols-4 grid-rows-4 gap-4">
        <div class="col-span-3 row-span-4">
          <p class="flex items-center justify-center">
            <iframe title="Stock Chart" frameBorder='0' scrolling='no' width='800' height='420' src='https://api.stockdio.com/visualization/financial/charts/v1/HistoricalPrices?app-key=8534C99CCADD4AFDB1D17BD809453DD7&indicators=BollingerBands(10,2.0);&stockExchange=TWSE&symbol={stock_id}&days=180&displayPrices=Candlestick&dividends=true&splits=true&motif=Block&palette=Aurora&googleFont=true'></iframe>
          </p>
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="股價淨值評估">
          {#if search_done}
            <p class="text-center">
              <strong>
                {stock_detail.bookValue_evaulate}
              </strong>
            </p>
          {:else}
            <span class="items-center loading loading-spinner loading-lg"></span>
          {/if}
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="現金股利評估">
          {#if search_done}
            <p class="text-center">
              <strong>
                {stock_detail.dividend_evaulate}
              </strong>
            </p>
          {:else}
            <span class="items-center loading loading-spinner loading-lg"></span>
          {/if}
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="股價淨值評估合理價">
          {#if search_done}
            <p class="text-center">
              <strong>
                {stock_detail.bookValue}
              </strong>
            </p>
          {:else}
            <span class="items-center loading loading-spinner loading-lg"></span>
          {/if}
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="現金股利評估合理價">
          {#if search_done}
            <p class="text-center">
              <strong>
                {stock_detail.fair_price}
              </strong>
            </p>
          {:else}
            <span class="items-center loading loading-spinner loading-lg"></span>
          {/if}
        </div>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <!-- if there is a button, it will close the modal -->
          <button class="btn">Close</button>
        </form>
      </div>
    </div>
</dialog>

<!-- iframe  -->
<!-- <iframe frameBorder='0' scrolling='no' width='800' height='420' src='https://api.stockdio.com/visualization/financial/charts/v1/HistoricalPrices?app-key=8534C99CCADD4AFDB1D17BD809453DD7&indicators=BollingerBands(10,2.0);&stockExchange=TWSE&symbol=2498&days=180&displayPrices=Candlestick&dividends=true&splits=true&motif=Block&palette=Aurora&googleFont=true'></iframe> -->