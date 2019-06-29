<template>
  <div class="author">
		<a href="/">
    <g-image
      alt="Author image"
      class="author__image"
      src="~/assets/images/Daniel+Greenfeld.jpeg"
      width="180"
      height="180"
      blur="5"
    />
		</a>

    <h1 v-if="showTitle" class="author__site-title">{{ $static.metaData.siteName }}</h1>

    <p
      class="author__intro"
    >I'm Daniel Roy Greenfeld, and welcome to my blog. I write about Python, Django, JavaScript, and more.</p>

    <p class="author__links">
      <a href="//twitter.com/pydanny">Follow me on Twitter</a>
      <a href="//github.com/pydanny">GitHub</a>
			<a href="/about">About</a>
    </p>
  </div>
</template>

<static-query>
query {
  metaData {
    siteName
  }
}
</static-query>

<script>
export default {
  props: ["showTitle"]
};
</script>

<style lang="scss">
.author {
  margin: 0 auto;
  max-width: 500px;
  text-align: center;
  padding: calc(var(--space) / 2) 0;

  &__image {
    border-radius: 100%;
    width: 90px;
    height: 90px;
    margin-bottom: 1em;
  }

  &__intro {
    opacity: 0.8;
  }

  &__site-title {
    font-size: 1.5em;
  }

  &__links {
    margin-top: -0.5em;
    a {
      margin: 0 0.5em;
    }
  }
}
</style>