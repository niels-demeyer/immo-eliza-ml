<!-- src/routes/page.svelte -->
<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import { Card } from "$lib/components/ui/card";
</script>


<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap w-full mb-20 flex-col items-center text-center">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-2 text-gray-900">Real Estate Price Estimator</h1>
      <p class="lg:w-1/2 w-full leading-relaxed text-gray-500">Choose between a house or apartment, select all your features and then click on estimate</p>
    </div>
    <div class="flex flex-wrap -m-4">
    </div>
    <div>
        <Card>
            <div class="flex flex-wrap -m-4">
                <div class="p-4 md:w-1/2">
                    <div class="h-full bg-gray-100 p-8 rounded">
                        <h2 class="text-xs title-font font-medium text-gray-500 tracking-widest">HOUSE</h2>
                        <h1 class="text-2xl font-medium text-gray-900">House</h1>
                        <p class="leading-relaxed mb-6">Choose this option if you want to estimate the price of a house</p>
                        <Button>Choose</Button>
                    </div>
                </div>
                <div class="p-4 md:w-1/2">
                    <div class="h-full bg-gray-100 p-8 rounded">
                        <h2 class="text-xs title-font font-medium text-gray-500 tracking-widest">APARTMENT</h2>
                        <h1 class="text-2xl font-medium text-gray-900">Apartment</h1>
                        <p class="leading-relaxed mb-6">Choose this option if you want to estimate the price of an apartment</p>
                        <Button>Choose</Button>
                    </div>
                </div>
            </div>
        </Card>
    </div>
    <button class="flex mx-auto mt-16 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Estimate</button>
  </div>
</section>