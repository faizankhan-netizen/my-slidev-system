<template>
  <div class="slidev-layout" :class="$frontmatter.class">
    <div class="content-wrapper" style="width: 100%; height: 100%; display: flex; flex-direction: column;">
      <slot />
    </div>
  </div>
</template>
