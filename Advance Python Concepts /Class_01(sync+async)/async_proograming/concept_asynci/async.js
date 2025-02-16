// Simulate async behavior with setTimeout to mimic asyncio.sleep
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function makeCoffeeAsync() {
    console.log("making coffee");
    await sleep(5000); // 5 seconds delay
    console.log(`coffee is ready at ${Date.now()}`);
}

async function makeToastAsync() {
    console.log("making toast");
    await sleep(3000); // 3 seconds delay
    console.log("toast is ready");
}

async function makeEggsAsync() {
    console.log("making eggs");
    await sleep(5000); // 5 seconds delay
    console.log("eggs are ready");
}

async function breakfastAsync() {
    await Promise.all([makeCoffeeAsync(), makeToastAsync(), makeEggsAsync()]);
}

// Run the breakfast function
breakfastAsync();


// withou async await
function makeCoffee() {
    console.log("making coffee");
    sleep(5000).then(() => {
        console.log(`coffee is ready at ${Date.now()}`);
    });
}

function makeToast() {
    console.log("making toast");
    sleep(3000).then(() => {
        console.log("toast is ready");
    });
}

function makeEggs() {
    console.log("making eggs");
    sleep(5000).then(() => {
        console.log("eggs are ready");
    });
}

function breakfast() {
    makeCoffee();
    makeToast();
    makeEggs();
}

// Run the breakfast function



// async await but  without sleep function
async function makeCoffeeAsync() {
    console.log("making coffee");
    await new Promise(resolve => setTimeout(resolve, 5000)); // 5 seconds delay
    console.log(`coffee is ready at ${Date.now()}`);
}

async function makeToastAsync() {
    console.log("making toast");
    await new Promise(resolve => setTimeout(resolve, 3000)); // 3 seconds delay
    console.log("toast is ready");
}

async function makeEggsAsync() {
    console.log("making eggs");
    await new Promise(resolve => setTimeout(resolve, 5000)); // 5 seconds delay
    console.log("eggs are ready");
}

async function breakfastAsync() {
    await Promise.all([makeCoffeeAsync(), makeToastAsync(), makeEggsAsync()]);
}


// Run the breakfast function

