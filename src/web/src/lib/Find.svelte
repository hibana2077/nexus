<script>
// @ts-nocheck
    import Profile from "./Profile.svelte";
    import { writable } from "svelte/store";
    import Singalcard from "./Singalcard.svelte";

    const StockCatData = [
    {
        id: "01",
        name: "水泥工業",
        value: "01"
    },
    {
        id: "16",
        name: "觀光餐旅",
        value: "16"
    },
    {
        id: "29",
        name: "電子通路業",
        value: "29"
    },
    {
        id: "02",
        name: "食品工業",
        value: "02"
    },
    {
        id: "17",
        name: "金融保險",
        value: "17"
    },
    {
        id: "30",
        name: "資訊服務業",
        value: "30"
    },
    {
        id: "03",
        name: "塑膠工業",
        value: "03"
    },
    {
        id: "31",
        name: "其他電子業",
        value: "31"
    },
    {
        id: "04",
        name: "紡織纖維",
        value: "04"
    },
    {
        id: "19",
        name: "綜合",
        value: "19"
    },
    {
        id: "32",
        name: "文化創意業",
        value: "32"
    },
    {
        id: "05",
        name: "電機機械",
        value: "05"
    },
    {
        id: "20",
        name: "其他",
        value: "20"
    },
    {
        id: "33",
        name: "農業科技業",
        value: "33"
    },
    {
        id: "06",
        name: "電器電纜",
        value: "06"
    },
    {
        id: "21",
        name: "化學工業",
        value: "21"
    },
    {
        id: "08",
        name: "玻璃陶瓷",
        value: "08"
    },
    {
        id: "22",
        name: "生技醫療業",
        value: "22"
    },
    {
        id: "35",
        name: "綠能環保",
        value: "35"
    },
    {
        id: "09",
        name: "造紙工業",
        value: "09"
    },
    {
        id: "23",
        name: "油電燃氣業",
        value: "23"
    },
    {
        id: "36",
        name: "數位雲端",
        value: "36"
    },
    {
        id: "10",
        name: "鋼鐵工業",
        value: "10"
    },
    {
        id: "24",
        name: "半導體業",
        value: "24"
    },
    {
        id: "37",
        name: "運動休閒",
        value: "37"
    },
    {
        id: "11",
        name: "橡膠工業",
        value: "11"
    },
    {
        id: "25",
        name: "電腦及週邊設備業",
        value: "25"
    },
    {
        id: "38",
        name: "居家生活",
        value: "38"
    },
    {
        id: "12",
        name: "汽車工業",
        value: "12"
    },
    {
        id: "26",
        name: "光電業",
        value: "26"
    },
    {
        id: "80",
        name: "管理股票",
        value: "80"
    },
    {
        id: "14",
        name: "建材營造",
        value: "14"
    },
    {
        id: "27",
        name: "通信網路業",
        value: "27"
    },
    {
        id: "15",
        name: "航運業",
        value: "15"
    },
    {
        id: "28",
        name: "電子零組件業",
        value: "28"
    }
];
    const url = 'http://0.0.0.0:8000/findstock';
    let select_condition = {
        cat: [],
        price: 25,
        dividend: 3,
        safety: 0.8
    }

    let stock_num = writable("");
    let stock_name = writable("");
    let have_a_search = writable(false);
    let searchjob_done = writable(false);
    let search_result = writable([]);
    let stock_detail = writable({
        bookValue_evaulate: "Loading",
        dividend_evaulate: "Loading",
        bookValue: "Loading",
        fair_price: "Loading"
    });

    function Search() {
        have_a_search.set(false);
        searchjob_done.set(false);
        let cat = [];
        document.querySelectorAll('.checkbox').forEach((el) => {
            if (el.checked) {
                cat.push(el.value);
            }
        });
        select_condition.cat = cat;
        select_condition.price = document.querySelector('#price').value;
        select_condition.dividend = document.querySelector('#dividend').value;
        select_condition.safety = document.querySelector('#safety').value;

        select_condition.price = select_condition.price.toString();
        select_condition.dividend = select_condition.dividend.toString();
        select_condition.safety = select_condition.safety.toString();

        console.log(select_condition);
        console.log(JSON.stringify(select_condition));
        have_a_search.set(true);

        // make a request to the server
        fetch(url, {
            method: 'POST',
            headers: {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(select_condition)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            searchjob_done.set(true);
            search_result.set(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    function showmore(stock_id, name) {
        stock_num.set(stock_id);
        stock_name.set(name);

        // search stock detail
        const url = 'http://0.0.0.0:8000/profile/singlestock';
        fetch(url, {
            method: 'POST',
            headers: {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                stock: stock_id,
                dividend_rate: document.querySelector('#dividend').value.toString(),
                safety: document.querySelector('#safety').value.toString()
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

        popup.showModal();
    }
</script>

<div class="flex items-center justify-center mt-8">
    <div class="bg-base-300 p-4 rounded-box shadow-xl w-112">
        <h2 class="text-2xl my-4 text-center">
            <strong>
            Find Stock
            </strong>
        </h2>
        <div class="divider divider-start">行業類別</div>
        <div class="form-control grid grid-cols-4">
            {#each StockCatData as cat}
            <label class="label cursor-pointer">
                <input type="checkbox" checked="checked" class="checkbox" value="{cat.id}" id="{cat.id}" />
                <span class="label-text flex grid justify-items-start">{cat.name}</span>
            </label>
            {/each}
        </div>
        <div class="divider divider-start">價格範圍</div>
        <input type="range" min="0" max="100" value="25" class="range" step="25" id="price" />
        <div class="w-full flex justify-between text-xs px-2">
        <span>0</span>
        <span>25</span>
        <span>50</span>
        <span>75</span>
        <span>>100</span>
        </div>
        <div class="divider divider-start">股息合理價-配息率</div>
        <input type="range" min="1" max="5" value="3" class="range" step="1" id="dividend" />
        <div class="w-full flex justify-between text-xs px-2">
        <span>1%</span>
        <span>2%</span>
        <span>3%</span>
        <span>4%</span>
        <span>5%</span>
        </div>
        <div class="divider divider-start">股息合理價-安全係數</div>
        <input type="range" min="0" max="1" value="0.8" class="range" step="0.2" id="safety" />
        <div class="w-full flex justify-between text-xs px-2">
        <span>0</span>
        <span>0.2</span>
        <span>0.4</span>
        <span>0.6</span>
        <span>0.8</span>
        <span>1</span>
        </div>
        <div class="divider"></div>
        <div class="grid grid-cols-3">
            <div></div>
            <div></div>
            <button class="btn btn-primary" on:click={Search}>
                Search
            </button>
        </div>
    </div>
</div>

<h2 class="text-2xl my-4 text-center">
    <strong>
    Stock List
    </strong>
</h2>

<div class="flex items-center justify-center mt-8">
    {#if $have_a_search && $searchjob_done}
        <div class="grid grid-cols-2 gap-4">
            {#each $search_result as stock}
                <Singalcard stock_basic_info={stock} showmore={showmore} />
            {/each}
        </div>
    {:else if $have_a_search && !$searchjob_done}
        <span class="loading loading-ring loading-lg"></span>
    {:else}
        <span></span>
    {/if}
</div>

{#if $have_a_search && $searchjob_done}
    <Profile stock_id={$stock_num} dialog_id="popup" stock_name={$stock_name} bookValue_evaulate={$stock_detail.bookValue_evaulate} dividend_evaulate={$stock_detail.dividend_evaulate} bookValue={$stock_detail.bookValue} fair_price={$stock_detail.fair_price} />
{/if}