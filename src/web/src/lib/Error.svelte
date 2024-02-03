<script>
    export let changePage;
</script>

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