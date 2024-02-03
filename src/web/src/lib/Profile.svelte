<script>
    export let stock_id = 'ID';
    export let dialog_id = 'no-name';
</script>

<dialog id={dialog_id} class="modal">
    <div class="modal-box w-11/12 max-w-5xl">
      <h3 class="font-bold text-lg">Stock ID: {stock_id}</h3>
      <p class="py-4">Click the button below to close</p>
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