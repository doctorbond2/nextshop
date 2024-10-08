export type TYPE_SubmitContext = {
  setSubmitData: any;
  submitData: any;
  resetSubmit: () => void;
  submit: <T extends keyof TYPE_SubmitData>(
    data: TYPE_SubmitData[T],
    type: T
  ) => void;
};
export type TYPE_LoginData = {
  password?: string;
  'user-login-username-or-email'?: string;
  email?: string;
  username?: string;
};

export type TYPE_RegisterData = {
  email: string;
  username: string;
  password: string;
};
export type TYPE_PasswordChangeData = {
  old_password: string;
  new_password: string;
};
export type TYPE_SubmitData = {
  login?: TYPE_LoginData;
  register?: TYPE_RegisterData;
  password_change: TYPE_PasswordChangeData;
};
