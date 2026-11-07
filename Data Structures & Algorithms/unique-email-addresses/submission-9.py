class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 1. clean the address
        cleaned = []

        for addi in emails:
            # preserve the domain
            local = addi.split('@')[0]
            domain = addi.split('@')[1]

            local = local.replace('.', '')
            local = local.split('+', 2)[0]
            cleaned.append([local + domain])

        # 2. count unique ones (set?)
        unique = []

        for c in cleaned:
            if c not in unique:
                unique.append(c)
        return len(unique)