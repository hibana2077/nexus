<script>
    export let showmore;

    export let stock_basic_info = {
        name: "台積電",
        code: "2330",
        price: 500,
        prev_day_change: 5,
        week_52_change_percent: 20,
        eps: 32.32,
        income: 83.371,
        ai_recommend: "Good"
    }

    let stock_color_set ={
        prev_day_change: stock_basic_info.prev_day_change > 0 ? "text-green-500" : stock_basic_info.prev_day_change < 0 ? "text-red-500" : "text-gray-500",
        week_52_change_percent: stock_basic_info.week_52_change_percent > 0 ? "text-green-500" : stock_basic_info.week_52_change_percent < 0 ? "text-red-500" : "text-gray-500",
        eps: stock_basic_info.eps > 0 ? "text-green-500" : stock_basic_info.eps < 0 ? "text-red-500" : "text-gray-500",
        income: stock_basic_info.income > 0 ? "text-green-500" : stock_basic_info.income < 0 ? "text-red-500" : "text-gray-500",
        ai_recommend: stock_basic_info.ai_recommend === "Good" ? "text-green-500" : stock_basic_info.ai_recommend === "Bad" ? "text-red-500" : "text-gray-500"
    }
</script>

<div class="w-96 h-60 bg-base-200 rounded-box grid grid-cols-5 grid-rows-5 gap-2 p-4">
    <div class="bg-base-300 hover:border-solid hover:border-2 rounded-box hover:border-primary row-span-3 col-span-4 tooltip" data-tip="股票名稱">
        <div class="grid grid-cols-2">
            <div class="col-span-1">
                <h2 class="text-2xl text-center mt-6">
                    <strong>
                    {stock_basic_info.name}
                    </strong>
                </h2>
            </div>
            <div class="col-span-1">
                <h2 class="text-2xl text-center mt-6">
                    <strong class="{stock_color_set.prev_day_change}">
                    {stock_basic_info.price}
                    </strong>
                </h2>
            </div>
        </div>
        <div class="grid grid-cols-2">
            <div class="col-span-1">
                <h2 class="text-xl text-center mb-6">
                    <strong>
                    {stock_basic_info.code}
                    </strong>
                </h2>
            </div>
            <div class="col-span-1">
                <h2 class="text-xl text-center mb-6">
                    <strong class="{stock_color_set.prev_day_change}">
                    {#if stock_basic_info.prev_day_change > 0}
                        + {stock_basic_info.prev_day_change}
                    {:else if stock_basic_info.prev_day_change < 0}
                        {stock_basic_info.prev_day_change}
                    {:else}
                        {stock_basic_info.prev_day_change}
                    {/if}
                    </strong>
                </h2>
            </div>
        </div>
    </div>
    <div class="bg-base-300 hover:border-solid hover:border-2 rounded-box hover:border-primary row-span-3 col-span-1 tooltip" data-tip="52週變化">
        <div class="text-center my-8 text-base {stock_color_set.prev_day_change}">
            {#if stock_basic_info.week_52_change_percent > 0}
                {stock_basic_info.week_52_change_percent}%
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-auto fill-green-500" viewBox="0 0 512 512"><path d="M414 321.94L274.22 158.82a24 24 0 00-36.44 0L98 321.94c-13.34 15.57-2.28 39.62 18.22 39.62h279.6c20.5 0 31.56-24.05 18.18-39.62z"/></svg>
            {:else if stock_basic_info.week_52_change_percent < 0}
                {stock_basic_info.week_52_change_percent}%
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-auto fill-red-500" viewBox="0 0 512 512"><path d="M98 190.06l139.78 163.12a24 24 0 0036.44 0L414 190.06c13.34-15.57 2.28-39.62-18.22-39.62h-279.6c-20.5 0-31.56 24.05-18.18 39.62z"/></svg>
            {:else}
                {stock_basic_info.week_52_change_percent}%
            {/if}
            
        </div>
    </div>
    <div class="bg-base-300 hover:border-solid hover:border-2 rounded-box hover:border-primary row-span-2 col-span-3 tooltip" data-tip="股票資訊">
        <div class="grid grid-cols-2">
            <div class="col-span-1">
                <h2 class="text-xl text-center my-2">
                    EPS<br/>
                    <strong class="{stock_color_set.eps}">
                    {stock_basic_info.eps}
                    </strong>
                </h2>
            </div>
            <div class="col-span-1">
                <h2 class="text-xl text-center my-2">
                    每股收入
                    <strong class="{stock_color_set.income}">
                    {stock_basic_info.income}
                    </strong>
                </h2>
            </div>
        </div>
    </div>
    <button class="bg-base-300 rounded-box row-span-2 col-span-2 hover:glass transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300 tooltip" data-tip="Click to see more" on:click={() => showmore(stock_basic_info.code, stock_basic_info.name)}>
        <div class="text-center my-6 text-xl {stock_color_set.ai_recommend}">
            <!-- AI recommend -->
            <strong>
            {stock_basic_info.ai_recommend}
            </strong>
        </div>
    </button>
</div>