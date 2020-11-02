<template>
  <div class="sequence">
    <div v-if="sequence">
      <h4>{{sequence.name}}</h4>
      <div v-for="(step,index) in sequence.steps" :key="index">
        <test-step
          class="step"
          :index="index"
          :step="step"
          :next-disabled="isNextDisabled"
          :class="{minimized: index != stepNumber}"
          @back="stepNumber--"
          @next="onNextStep"
          >
        </test-step>
      </div>
    </div>
  </div>
</template>

<script>
// Create hash to force reload of TestStep.vue
let hash = Math.random().toString(36).substring(2, 8);
let qhash = `?${hash}`;
module.exports = {
  props: ['test'],
  components: {
    'test-step': httpVueLoader('./TestStep.vue' + qhash),
  },
  data: function() {
    return {
      sequence: null,
      stepNumber: 0,
    }
  },  // data
  methods: {
    onNextStep: function(action) {
      if (action != 'play') {
        this.stepNumber++;
        return;
      }

      // (else) Advance to end step
      console.log('Advancing to *end* step.');
      // Advance to the "end" step
      let endNumber = null;
      for (let i = this.stepNumber; i < this.sequence.steps.length; ++i) {
        if ('end' in this.sequence.steps[i]) {
          endNumber = i;
          this.stepNumber = i;
          break;
        }
      }
      if (endNumber == null) {
        alert('Could not find matching "end" step - something is broken in the test script.');
      }
    },  // onNextStep()
    startTest: function() {
      // console.log(`TestRunner updating test ${this.test}`);
      let ts = Date.now();
      let filename = `data/${this.test}.json?${ts}`;
      axios.get(filename)
        .then(response => {
          this.sequence = response.data;
          this.stepNumber = 0;
        })
        .catch(function(error) {console.error(error)});
    },  // startTest()
  },  // methods
  computed: {
    isNextDisabled: function() {
      let last = this.sequence.steps.length - 1;
      return this.stepNumber === last;
    }
  },  // computed
  mounted: function() {
    this.startTest();
  },  // mounted()
  watch: {
    test: function(newVal, oldVal) {
      // console.log(`TestRunner: test changed to ${newVal}`);
      this.startTest();
    }
  },  // watch
}
</script>

<style scoped>
  button {
    margin-right: 1em;
  }
</style>
