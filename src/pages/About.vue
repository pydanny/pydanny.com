<template>
  <Layout :show-logo="false">

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

        <p class="author__links">
          <a href="//twitter.com/pydanny">Twitter</a>
          <a href="//github.com/pydanny">GitHub</a>
          <a href="//www.linkedin.com/in/pydanny/">LinkedIn</a>
          <a href="//roygreenfeld.com">Roy Greenfeld</a>
        </p>
  </div>

    <div class="content-box">
      <div class="post__content">       

        <p>About Daniel Roy Greenfeld</p>

        <p><strong>Daniel Roy Greenfeld</strong> has over {{ new Date().getFullYear() - 1997 }} years of experience in the technology industry and a depth of knowledge in computer programming languages including Python, Django, JavaScript, and Vue.js. He previously worked as a software engineer for NASA where he twice earned an Award for Excellence for his work on numerous large-scale software systems. Daniel also co-authored the <a href="https://twoscoopspress.com">Two Scoops of Django: Best Practices</a> book series and created numerous large open-source projects such as Cookiecutter Django. He is a Fellow of the Python Software Foundation and received the Frank Willison Memorial Award for contributions to Python. At <a href="https://britecore.com">BriteCore</a>, Daniel serves as VP of Implementation Engineering, where he oversees various aspects of engineering.</p>

        <p>In his free time, Daniel enjoys spending time with his wife and daughter, contributing to open source, writing fantasy and science fiction, and cycling.</p>
      </div>
    </div>
  </Layout>
</template>

<script>
export default {
  metaInfo: {
    title: "About Daniel Roy Greenfeld"
  }
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
