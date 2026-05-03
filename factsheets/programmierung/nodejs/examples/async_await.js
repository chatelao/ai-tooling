function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  console.log('Waiting 1 second...');
  await delay(1000);
  console.log('Done!');
}

run();
