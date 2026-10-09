/**
 * Cloudflare Worker — Carolina García B. — Static Site
 * Workers Assets serving
 */
export default {
  async fetch(request, env, ctx) {
    const path = new URL(request.url).pathname;
    if (path.split('/').some(part => part.startsWith('.')) ||
        /^(?:\/README\.md|\/PROMPT-HERMES\.md|\/wrangler\.toml|\/src(?:\/|$))/i.test(path)) {
      return new Response('Not found', {status: 404});
    }
    return env.ASSETS.fetch(request);
  }
};
