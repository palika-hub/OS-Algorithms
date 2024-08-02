#include <windows.h>
#include <winhttp.h>
#include <iostream>

#pragma comment(lib, "winhttp.lib")

void HandleHttpRequest(HINTERNET hRequest) {
    DWORD bytesRead = 0;
    CHAR buffer[4096];

    while (WinHttpReadData(hRequest, buffer, sizeof(buffer), &bytesRead) && bytesRead > 0) {
        std::cout.write(buffer, bytesRead);
    }
}

void StartServer() {
    HINTERNET hSession = WinHttpOpen(L"SimpleServer", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY, WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);
    if (hSession) {
        HINTERNET hConnect = WinHttpOpenRequest(hSession, L"GET", L"/", NULL, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, 0);
        if (hConnect) {
            if (WinHttpSendRequest(hConnect, WINHTTP_NO_ADDITIONAL_HEADERS, 0, WINHTTP_NO_REQUEST_DATA, 0, 0, 0)) {
                if (WinHttpReceiveResponse(hConnect, NULL)) {
                    // Wait for the server to finish responding
                    DWORD statusCode = 0;
                    DWORD statusCodeSize = sizeof(statusCode);
                    WinHttpQueryHeaders(hConnect, WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER, NULL, &statusCode, &statusCodeSize, NULL);

                    if (statusCode == HTTP_STATUS_OK) {
                        HandleHttpRequest(hConnect);
                    } else {
                        std::cerr << "Error: Unexpected status code " << statusCode << std::endl;
                    }
                }
            }

            WinHttpCloseHandle(hConnect);
        }

        WinHttpCloseHandle(hSession);
    }
}

int main() {
    if (!WinHttpCheckPlatform()) {
        std::cerr << "Error: WinHTTP is not available on this platform." << std::endl;
        return 1;
    }

    StartServer();

    return 0;
}
