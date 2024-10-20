import { test, expect, request } from '@playwright/test';

const BASE_URL = 'YOUR_API_BASE_URL'; // Replace with your actual API base URL

test.describe('API Tests', () => {
  let token: string;

  test('Verify API health', async ({ request }) => {
    const response = await request.get(`${BASE_URL}/health`);
    expect(response.status()).toBe(200);
    expect(await response.json()).toEqual({ status: 'ok' }); // Adjust expected response
  });

  test('Register a new user', async ({ request }) => {
    const response = await request.post(`${BASE_URL}/users/register`, {
      data: {
        // Provide registration data (username, email, password, etc.)
      },
    });
    expect(response.status()).toBe(201); // Assuming 201 Created
    expect(await response.json()).toHaveProperty('message', 'User registered successfully'); // Adjust expected response
  });

  test('Login with a user', async ({ request }) => {
    const response = await request.post(`${BASE_URL}/users/login`, {
      data: {
        // Provide login credentials (username/email, password)
      },
    });
    expect(response.status()).toBe(200);
    const responseData = await response.json();
    expect(responseData).toHaveProperty('token');
    token = responseData.token; // Store the token for subsequent requests
  });

  test('Get user profile', async ({ request }) => {
    const response = await request.get(`${BASE_URL}/users/profile`, {
      headers: {
        Authorization: `Bearer ${token}`, // Include the token in the header
      },
    });
    expect(response.status()).toBe(200);
    const profileData = await response.json();
    // Verify profile information
  });

});
