/**
 * Cloudflare Worker — Carolina García B. — Static Site
 * Workers Assets serving
 */
export default {
  async fetch(request, env, ctx) {
    return env.ASSETS.fetch(request);
  }
};
