class _Soln:
    def check_dom(self, str_param: str) -> bool or str:
        """
        Check if an HMTL tag is valid or not.

        Args:
            str_param(str): An input HTML string containing tags.
        
        Return:
            bool or str: Return False if HTML tags are mismatched or invalid
                        Returns mismatched tag if there's only one.
                        Returns True if all tags are matched and valid.
        Examples:
            >>> check_dom("<p>Hello World!</p>")
            True
            
            >>> check_dom("<p>Hello World!</i>")
            'p'

            >>> check_dom("<p>Hello World!")
            False

        HTML Tags to be used:
            The elements that will be used are: <b>, <i>, <em>, <div>, <p>
        """
        tags = ('<b>', '<i>', '<em>', '<div>', '<p>')
        mismatched_t = []
        matched_t = []

        # number of tags should be even, odd number of tags
        # implies invalid tags.
        if str_param.count('<') % 2 != 0 or str_param.count('>') % 2 != 0:
            return False
        if str_param.count('<') != str_param.count('>'):
            return False
        for k in tags:
            m = k[:1] + '/' + k[1:]
            if k in str_param and m in str_param:
                matched_t.append(k)
            elif k in str_param and m not in str_param:
                mismatched_t.append(k)
        # check if all tags are matched and return True
        if len(mismatched_t) == 0 and len(matched_t) >= 1:
            return True
        # return False for more than one mismatch tags
        if len(mismatched_t) == 1:
            return mismatched_t[0][1:2]
        else:
            return False
