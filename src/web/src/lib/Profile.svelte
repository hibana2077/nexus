<script>

  export let stock_id = 'ID';
  export let dialog_id = 'no-name';
  export let stock_name = '台積電';
  export let bookValue_evaulate = "Loading";
  export let dividend_evaulate = "Loading";
  export let bookValue = "Loading";
  export let fair_price = "Loading";

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
          <p class="text-center py-10">
            <strong>
              {bookValue_evaulate}
            </strong>
          </p>
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="現金股利評估">
          <p class="text-center py-10">
            <strong>
              {dividend_evaulate}
            </strong>
          </p>
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="股價淨值評估合理價">
          <p class="text-center py-10">
            <strong>
              {bookValue}
            </strong>
          </p>
        </div>
        <div class="hover:border-solid hover:border-2 rounded-box hover:border-primary bg-base-300 tooltip" data-tip="現金股利評估合理價">
          <p class="text-center py-10">
            <strong>
              {fair_price}
            </strong>
          </p>
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