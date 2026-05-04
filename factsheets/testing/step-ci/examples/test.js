module.exports = {
  tests: [
    {
      name: "Check Status",
      check: (response) => response.status === 200
    }
  ]
};
