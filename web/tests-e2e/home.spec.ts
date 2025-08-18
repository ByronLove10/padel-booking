import { test, expect } from "@playwright/test"

test("homepage loads and has title", async ({ page }) => {
  await page.goto("http://localhost:3000")
  await expect(page).toHaveTitle(/Next\.js|Create Next App/i)
})
