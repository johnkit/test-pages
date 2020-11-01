<template>
  <div>
    <div class="step-header">{{index + 1}}. {{step.title}}</div>
    <div class="step-content">
      <p><strong>Action: </strong><span v-html="step.action"></span></p>
      <p v-if="step.expect"><strong>Expect: </strong><span v-html="step.expect"></span></p>
      <div>
        <button :disabled="stepNumber == 0" @click="$emit('back')">Back</button>
        <button :disabled="nextDisabled" @click="$emit('next')">Next</button>
      </div>
    </div>
  </div>
</template>

<script>
module.exports = {
  props: ['index', 'step', 'stepNumber', 'nextDisabled'],
  events: ['back', 'next'],
  data: function() {
    return {
    }
  },  // data
  methods: {
  },  // methods
}
</script>

<style scoped>
</style>
