<template>
  <div class="home">
    <SegmentForm msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SegmentForm from '@/components/SegmentForm'

export default {
  name: 'Home',
  components: {
    SegmentForm
  }
}
</script>
